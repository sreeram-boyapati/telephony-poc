import os
import configparser

from os.path import join

from plivo import CONF_FILE, ROOT_DIR


class ConfigProvider(object):
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
            cls._instance.configs = None
        return cls._instance

    @classmethod
    def get_configs(cls):
        instance = cls.get_instance()

        if instance.configs is None:
            instance.configs = cls.load_configs()

        return instance.configs

    @classmethod
    def load_configs(cls):
        assert os.path.isfile(CONF_FILE), "Configuration file is not Present"
        fp = open(CONF_FILE)
        config_reader = configparser.ConfigParser()
        config_reader.read_file(fp)
        configs = config_reader['DEFAULT']
        fp.close()
        return configs


class AppConfig(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + join(ROOT_DIR, 'sqlite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ConfigProvider.get_configs()['SECRET_KEY']
    WTF_CSRF_ENABLED = False
