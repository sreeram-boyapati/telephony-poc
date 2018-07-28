import json

from datetime import datetime, timedelta

from plivo.app import app
from plivo.models.sms import SMS

from fixtures import test_client as client
from fixtures import redis_client as cache


def test_same_number(client):
    resp = client.post('/outbound/sms', headers={
        'Authorization': 'Basic dGVzdDp0ZXN0',
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'from': '91987654321',
        'to': '91987654321',
        'text': 'asdas'
    }))

    assert resp.status_code == 400


def test_success_resp(client, cache):
    resp = client.post('/outbound/sms', headers={
        'Authorization': 'Basic dGVzdDp0ZXN0',
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'from': '91987654322',
        'to': '91987654321',
        'text': 'asdas'
    }))

    headers = resp.headers
    header_keys = map(lambda x: x[0], headers)

    assert "X-Rate-Limit-Value" in header_keys
    assert "X-Rate-Limit-Threshold" in header_keys

    for header in headers:
        if header[0] is "X-Rate-Limit-Value":
            assert header[1] == '1'


    assert resp.status_code == 200

    resp = client.post('/outbound/sms', headers={
        'Authorization': 'Basic dGVzdDp0ZXN0',
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'from': '91987654322',
        'to': '91987654321',
        'text': 'asdas'
    }))

    headers = resp.headers
    for header in headers:
        if header[0] is "X-Rate-Limit-Value":
            assert header[1] == '2'


def test_missing_param(client, cache):
    resp = client.post('/outbound/sms', headers={
        'Authorization': 'Basic dGVzdDp0ZXN0',
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'from': '91987654322',
        'text': 'asdas'
    }))

    assert resp.status_code == 400


def test_rate_limit_exceeded(client, cache):
    payload = {
        'from': '91987654322',
        'to': '91987654321',
        'text': 'asdas'
    }

    now = datetime.now()
    hour = now.hour

    key = "ratelimit:{}:{}".format(payload['from'], str(hour))
    cache.setex(key, 3600, 50)

    resp = client.post('/outbound/sms', headers={
        'Authorization': 'Basic dGVzdDp0ZXN0',
        'Content-Type': 'application/json'
    }, data=json.dumps({
        'from': '91987654322',
        'to': '91987654321',
        'text': 'asdas'
    }))

    assert resp.status_code == 429
