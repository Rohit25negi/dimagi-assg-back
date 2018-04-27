"""
learning.resources.registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module defines the registration resource which is used to register a 
particular user.

"""


from flask_jwt_extended import create_access_token
from flask_restful import reqparse

from learning.database.user_model import UserModel
from learning.resources.base_resource import BaseResource


class Register(BaseResource):
    '''
    Register resource handles the request at /register endpoint
    '''

    def post(self):
        """
        Method handles the request at /register endpoint and responsible
        for registering a new entry for a new user.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', required=True)
        parser.add_argument('last_name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        arg_dict = parser.parse_args()
        response = dict()
        if not UserModel.find_by_condition({"email":arg_dict.get('email')}):
            user = self.add_user(arg_dict)
            acces_token = create_access_token(identity=user.email)
            response['access_token'] = acces_token
            response['message'] = 'user_created'
        else:
            response['message'] = 'user already exists'
        return response

    def add_user(self, arg_dict):
        """
        Method adds the user into the database.

        Parameters
        -----------
        arg_dict: dict
            dictionary containing the user information
        
        Returns
        --------
        user: UserModel
            Object of User Model
        """
        user = UserModel(**arg_dict)
        user.save_to_db()
        return user
