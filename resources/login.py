'''
learning.resources.login
~~~~~~~~~~~~~~~~~~~~~~~~~
Module defines the login resoure

'''

from flask_jwt_extended import create_access_token, set_access_cookies
from flask_restful import reqparse
from flask import  jsonify

from learning.database.user_model import UserModel
from learning.resources.base_resource import BaseResource


class Login(BaseResource):
    """
    Login resource which is used to prepare the jwt tooken for the user
    """

    def post(self):
        """
        handles the POST request on /login endpoint.
        It is used  when user wants to login. This returns the jwt access token.
        if the credentials are right.

        """
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)

        argument_dict = parser.parse_args()

        user_email = argument_dict.get("email")
        user_password = argument_dict.get('password')
        response = dict()
        user = UserModel.find_by_condition({'email': user_email})
        if user:
            if UserModel.verify_hash(user_password, user.password):
                access_token = create_access_token(identity=user_email)
                response['access_token'] = access_token
                response['message'] = 'Logged In'
                response = jsonify(response)
                set_access_cookies(response, access_token)
            else:
                response['message'] = 'incorrect Password'
        else:
            response['message'] = 'User does not exists'

        return response
