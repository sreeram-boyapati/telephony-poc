from plivo.app import app

from fixtures import test_client


def test_post_inbound_sms(test_client):
    client = app.test_client()

    client.post('/inbound/sms', )
