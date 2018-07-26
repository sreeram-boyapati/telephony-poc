from os.path import dirname, join, abspath

ROOT_DIR = abspath(dirname(dirname(__file__)))
SOURCE_DIR = abspath(dirname(__file__))
CONF_DIR = join(SOURCE_DIR, 'config')
CONF_FILE = join(CONF_DIR, 'env.ini')
#CONF_FILE = join(CONF_DIR, 'env.heroku.ini')
