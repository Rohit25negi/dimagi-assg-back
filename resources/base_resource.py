"""
learning.resources.base_resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module defines a base resource module for all the resources for the code
resuability by inheritance.
"""

from flask_restful import Resource


class BaseResource(Resource):
    """
    Base resource which will contain the common functionalites of 
    all its sub resources.
    """
