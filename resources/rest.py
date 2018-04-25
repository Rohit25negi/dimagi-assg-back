"""
learning.resource.rest
~~~~~~~~~~~~~~~~~~~~~~
Module defines function used to setup the rest resources of the application


"""


from learning.application_vars import API
from learning.resources.location_resource import LocationResource
from learning.resources.login import Login
from learning.resources.registeration import Register


def register_api():
    """
    function register the rest resources with the api endpoint of the application

    
    """
    API.add_resource(LocationResource, "/user-location")
    API.add_resource(Login, '/login')
    API.add_resource(Register, '/register')
