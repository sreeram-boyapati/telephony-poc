import base64

from plivo.app import app

from fixtures import test_client as client


def test_post_inbound_sms(client):
    auth = "test:test"
    b64_value = base64.b64encode(auth)

    resp = client.post('/inbound/sms', headers={
        'Authorization': 'Basic %s'.format(b64_value)
    }, data={
        'from': 91987654321,
        'to': 91987654321,
    })
    assert resp.status_code == 400

