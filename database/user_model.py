"""
database.user_model
~~~~~~~~~~~~~~~~~~~~

Module defines the UserModel. This model represents the 'users' table
in the database.
"""

from passlib.hash import pbkdf2_sha256 as sha256

from learning.application_vars import DB
from learning.database.Entity import BaseModel
from learning.database import constants as cnsts


class UserModel(BaseModel, DB.Model):
    """
    UserModel represents the 'users' table in database. It's object represents
    a single user.
    """
    __tablename__ = cnsts.USER_TABLE_NAME

    first_name = DB.Column(DB.String())
    last_name = DB.Column(DB.String())
    email = DB.Column(DB.String(), unique=True)
    password = DB.Column(DB.String())


    def __init__(self, first_name, last_name, email, password):
        """
        CONSTRUCTOR
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = UserModel.generate_hash(password)


    @staticmethod
    def generate_hash(password):
        """
        Method is used to create the hash of the password of the user
        
        Parameters
        -----------
        password: str
            password of the user
        """
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        """
        Method is used to verify the hash

        Parameters
        -----------
        password: str
            password of the user
        hash: str
            hash of the password which is to be varified against the password
        """
        return sha256.verify(password, hash)


    @staticmethod
    def find_by_condition(conditions):
        """
        Method finds and returns the user object which satisfies the condition
        given.

        Parameters
        -----------
        conditions: dict
            conditions here signifies the where condition in the sql query.
            Eg: {'email':'xyz@pqr.com'} will fit as:
            select * from users where email='xyz@pqr.com'
        """
        user_with_email = UserModel.query.filter_by(**conditions)

        if user_with_email:
            return user_with_email.first()
        else:
            return None
