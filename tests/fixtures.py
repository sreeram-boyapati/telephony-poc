import pytest

from plivo.app import app


@pytest.fixture
def test_client():
    app.test_client()
    app.config['BASIC_AUTH_USERNAME'] = 'test'
    app.config['BASIC_AUTH_PASSWORD'] = 'test'
    from plivo import routes
