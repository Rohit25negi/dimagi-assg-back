"""
learning.configuration
~~~~~~~~~~~~~~~~~~~~~~~
Module defines the configuration classes for the application

"""

from learning.database import credentials
from learning.resources import rest


class Config(object):
    """
    BASE configuration class
    """
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    """
    Production configuration classes\

    """
    SQLALCHEMY_DATABASE_URI = credentials.get_data_uri()
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_COOKIE_NAME = 'access_token_cookie'
    
    JWT_SECRET_KEY = 'asdfasdfsad'

class TestingConfig(Config):
    """
    Test configuraton class
    """
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = credentials.get_test_uri()
    JWT_SECRET_KEY = 'asdfasdfsad'



def configure_api():
    """
    function confugures the rest api of the app
    """
    rest.register_api()

def configure_app(app):
    """
    function configures the flask app 
    """

    app.config.from_object('learning.configuration.ProductionConfig')
    configure_api()
