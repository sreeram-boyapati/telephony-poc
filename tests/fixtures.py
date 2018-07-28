import pytest

from plivo.app import app, db
from plivo import routes
from plivo.providers.cache import RedisProvider


@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    # Clean all
    with app.app_context():
        client = app.test_client()
        client.testing = True
        db.create_all()
        yield client
        db.drop_all()


@pytest.fixture
def redis_client():
    instance = RedisProvider.get_instance()
    conn = instance.get_conn()
    yield conn
    clear_cache(conn, "ratelimit*")
    clear_cache(conn, "stop*")


def clear_cache(conn, pattern):
    cursor = '0'
    while cursor != 0:
        cursor, keys = conn.scan(cursor=cursor, match=pattern, count=5000)
        if keys:
            conn.delete(*keys)

    return True
