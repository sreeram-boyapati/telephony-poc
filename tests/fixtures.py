import pytest

from os.path import join

from plivo.app import app, db
from plivo import routes, ROOT_DIR
from plivo.providers.cache import RedisProvider


class TestAppConfig(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + join(ROOT_DIR, 'test_sqlite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'thisismylife'
    WTF_CSRF_ENABLED = False
    BASIC_AUTH_USERNAME = 'test'
    BASIC_AUTH_PASSWORD = 'test'


@pytest.fixture
def test_client():
    app.config.from_object(TestAppConfig)
    app.config['TESTING'] = True
    app.config['DEBUG'] = False
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
