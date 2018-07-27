import os
import redis


class RedisProvider(object):
    """Singleton class to provide redis client
    """
    instance = None

    @staticmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = RedisProvider()
        return cls.instance

    def get_conn(self):
        return redis.StrictRedis(
                host=os.environ.get('REDIS_HOST'),
                port=os.environ.get('REDIS_PORT'),
                db=os.environ.get('REDIS_DB'))
