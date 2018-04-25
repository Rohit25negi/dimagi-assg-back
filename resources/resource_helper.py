"""
learning.resource.resource_helper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
module defines the helper functions which are used in other modules in the resources

"""

import requests

from learning.database.user_model import UserModel


def user_exists(email):
    """
    Function checks if the user with email exists or not.
    if user exists then it returns the userModel object else returns None

    Parameters
    -----------
    email: str
        user email

    Returns
    --------
    UserModel| None
        Object of UserMole if the user with the given email exists. Else, None
    """
    user_search_condition = dict()
    user_search_condition['email'] = email

    return UserModel.find_by_condition(user_search_condition)


def send_get(url):
    """
    Function is used to send the get request and returns the json response.

    Parametrs
    ----------
    url: str
        url to which get request is to be sent

    Returns
    --------
    dict | None
        response in dict format if request happens properly. Else, return None
    """
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None


def verify_user(email,password):
    """
    function verifies the user creds

    Parameters
    -----------
    email: str
    password: str

    Returns
    --------
    bool:

    """
    user = user_exists(email)
    if user:
        return UserModel.verify_hash(password,user.password)

    return False
