import redis

from plivo.config import ConfigProvider


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
        configs = ConfigProvider().get_configs()
        return redis.StrictRedis(
                host=configs['REDIS_HOST'],
                port=configs['REDIS_PORT'],
                db=configs['REDIS_DB'])
