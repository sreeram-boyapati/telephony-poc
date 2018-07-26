from plivo.app import app
from flask_migrate import MigrateCommand
from flask_script import Manager

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# add db init tools

if __name__ == '__main__':
    manager.run()
