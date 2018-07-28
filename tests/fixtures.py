import pytest

from plivo.app import app
from plivo import routes


@pytest.fixture
def test_client():
    client = app.test_client()
    return client
