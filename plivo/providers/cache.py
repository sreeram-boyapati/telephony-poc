import os
import redis


class RedisProvider(object):
    """Singleton class to provide redis client
    """
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = RedisProvider()
        return cls.instance

    def get_conn(self):
        APP_MODE = os.environ.get('APP_MODE', 'dev')
        if APP_MODE == 'dev':
            return redis.StrictRedis(
                    host='localhost',
                    port='6379',
                    db='0')
        else:
            return redis.StrictRedis.from_url(os.environ.get('REDIS_URL'))
