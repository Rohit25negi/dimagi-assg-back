'''
database.Entity
~~~~~~~~~~~~~~~~

Module defines a base class for all the models. This base class can
contain the common attributes/methods which has to be shared among all the
child models.
'''

from learning.application_vars import DB


class BaseModel():
    """
    BaseModel works as a parent model for all the database model.
    It contains the common attributes and methods that can be shared
    among all the database models
    """
    id = DB.Column(DB.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    created_at = DB.Column(DB.DateTime(), server_default=DB.func.now())


    def save_to_db(self):
        """
        Method saves the current UserModel object to the database

        """
        DB.session.add(self)
        DB.session.commit()
