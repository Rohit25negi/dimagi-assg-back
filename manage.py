"""
asdf
asd
f
asd
fasd
f
sd
f

"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from flask_script import Command, Manager, Server

from learning.application import APP
from learning.application_vars import DB
from learning.configuration import configure_app


class CreateTables(Command):
    """Fills in predefined data to DB"""

    def run(self, **kwargs):
        """
        method is used to create the table schema into the database
        """
        DB.create_all()
        DB.session.commit()

configure_app(APP)

manager = Manager(APP)
manager.add_command('runserver', Server(host='0.0.0.0', port=5000))
manager.add_command('create_tables', CreateTables())


if __name__ == '__main__':
    manager.run()
