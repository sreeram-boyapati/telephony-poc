import json

from plivo.app import app
from plivo.models.sms import SMS

from fixtures import test_client as client
from fixtures import redis_client as cache


def test_same_number(client):
    resp = client.post('/inbound/sms', headers={
        'Authorization': 'Basic dGVzdDp0ZXN0',
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'from': '91987654321',
        'to': '91987654321',
        'text': 'asdas'
    }))

    assert resp.status_code == 400


def test_success_resp(client, cache):
    resp = client.post('/inbound/sms', headers={
        'Authorization': 'Basic dGVzdDp0ZXN0',
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'from': '91987654322',
        'to': '91987654321',
        'text': 'asdas'
    }))

    assert resp.status_code == 200


def test_missing_param(client, cache):
    resp = client.post('/inbound/sms', headers={
        'Authorization': 'Basic dGVzdDp0ZXN0',
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'from': '91987654322',
        'text': 'asdas'
    }))

    assert resp.status_code == 400


def test_stop(client, cache):
    payload = {
        'from': '91987654322',
        'to': '91987654321',
        'text': 'STOP'
    }

    resp = client.post('/inbound/sms', headers={
        'Authorization': 'Basic dGVzdDp0ZXN0',
        'Content-Type': 'application/json'
    }, data=json.dumps(payload))

    key = "stop:{}:{}".format(payload['from'], payload['to'])

    value = cache.get(key)

    assert value is not None
    assert resp.status_code == 200

    outbound_payload = {
        'from': payload['to'],
        'to': payload['from'],
        'text': 'asdad',
    }

    outbound_resp = client.post('/outbound/sms', headers={
        'Authorization': 'Basic dGVzdDp0ZXN0',
        'Content-Type': 'application/json'
    }, data=json.dumps(outbound_payload))

    assert outbound_resp.status_code == 400
