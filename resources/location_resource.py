"""
learning.resources.location_resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Module defines the Location resource which accepts the api requests at /user-location.
This resource is responsible for handling the user location.
"""

import ast
import os


from flask_restful import reqparse

from learning.database.user_location import LocationModel
from learning.resources import constants, resource_helper
from learning.resources.base_resource import BaseResource


class LocationResource(BaseResource):
    """
    Location resource is used to handle the user location. It recieves the following
    HTTP api request on /user-location:
        1. POST
    """

    def post(self):
        """
        method receives the http POST request on /user-location.
        This is hit when user want to update his location.

        Returns
        --------
        response: dict
            dictionary containing the response
        """
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=False)
        parser.add_argument('geoname_info', required=False)
        parser.add_argument('country', required=False)
        parser.add_argument('city', required=False)

        request_arguments = parser.parse_args()

        user_email = request_arguments.get('email')
        password = request_arguments.get('password')
        country = resource_helper.unicode_to_str(request_arguments.get('country'))
        city = resource_helper.unicode_to_str(request_arguments.get('city'))


        response = dict()

        if resource_helper.user_exists(user_email) and resource_helper.verify_user(user_email, password):

            if request_arguments.get('geoname_info'):
                geoname_info = ast.literal_eval(request_arguments.get('geoname_info'))
                if self.store_geo_location(user_email,geoname_info):
                    response['message'] = 'location is saved'
                    response['status'] = 'done'
                else:
                    response['message'] = 'could not save your location'
                    response['status'] = 'error'
            else:
                geoinformation = self.search_location(city, country)
                response = self.prepare_geo_data_response(user_email, geoinformation)

        else:
            response['message'] = 'Not a valid user'
            response['status'] = 'error'

        return response


    def search_location(self, city, country):
        """
        method takes city and country and search in geonames using an api call.

        Parameters
        -----------
        city: string
            name of the city
        country : string
            name of country
        
        Returns
        --------
        geoinformation: dict  
            dictionary, the response from the geoname api. this dict
            contains the information which matched with the given city and country
        """


        search_query = '{}, {}'.format(city, country)
        user_name = os.getenv('GEONAME_USER')
        user_pass = os.getenv('GEONAME_PASS')

        # TODO user validation
        api_url = constants.GEO_NAMES_API.format(
            search_query, user_name, user_pass)
        geoinformation = resource_helper.send_get(api_url)
        
        return geoinformation

    def prepare_geo_data_response(self, user_email, geoinformation):
        """
        Method prepare the request response depending on the geonames data.

        Parameters
        -----------
        email: str
            email of the user

        geoinformation: dict:
            dictionary, the response from the geoname api. this dict
            contains the information which matched with the given city and country

        Returns
        --------
        response: dict
            dictionary containing the response

        """
        response = dict()

        if not geoinformation.get('geonames'):
            response['message'] = 'no information for this geo location'
            response['status'] = 'error'

        elif len(geoinformation.get('geonames')) > 1:
            response['message'] = 'multiple matches for geo locations'
            response['location_result'] = self.parser_geoname_data(geoinformation)
            response['status'] = 'pending'
        else:
            if self.store_geo_location(user_email, geoinformation.get('geonames')[0]):
                response['message'] = 'location is saved'
                response['status'] = 'done'
        return response
        
    def parser_geoname_data(self, geoname_data):
        """
        Method parses the geonames data and extracts only the required information
        like:
            city name
            country name
            longitude
            latitude
        
        Parameters
        -----------
        geoname_data: dict
            dictionary, the response from the geoname api.
        
        Returns
        ---------
        parsed_geoname_data: list
            list of curated geolocation with the required information only
        
        """
        parsed_geoname_data = list()

        for geo_loc in geoname_data.get('geonames'):

            loc = dict()
            loc['name'] = geo_loc.get('name')
            loc['countryName'] = geo_loc.get('countryName')
            loc['lng'] = geo_loc.get('lng')
            loc['lat'] = geo_loc.get('lat')
            parsed_geoname_data.append(loc)

        return parsed_geoname_data

    def store_geo_location(self, user_email, geo_location):
        """
        Method stores the location into the location table into the database

        Parameters
        -----------
        user_email: str
            user email
        geo_location: dict
            dictionary containing the geo location
        

        Returns
        --------
        bool:

            True if the information is stored perfectly. Else, False.
        """
        try:
            country = geo_location.get('countryName')
            city = geo_location.get('name')
            lng = geo_location.get('lng')
            lat = geo_location.get('lat')

            user = resource_helper.user_exists(user_email)
            location = LocationModel(country=country, city=city,
                                     longitude=lng, latitude=lat, user_id=user.id)

            location.save_to_db()
            return True
        except Exception as error:
            # TODO log error
            print error
            return False
