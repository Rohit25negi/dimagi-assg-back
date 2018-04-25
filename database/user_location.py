'''
database.user_location
~~~~~~~~~~~~~~~~

Modules defines the LocationModel which is the OOPS representation of the
location table in the database. This table is used to store the user's informatio
into the database.
'''

from learning.application_vars import DB
from learning.database import constants as cnsts
from learning.database.Entity import BaseModel


class LocationModel(BaseModel, DB.Model):
    """
    Location model represents the location table in the database.
    This table is used to store the geolocation of the users
    It extends the BaseModel and DB.Model


    """
    __tablename__ = cnsts.USER_LOCATION
    country = DB.Column(DB.String())
    city = DB.Column(DB.String())
    longitude = DB.Column(DB.String())
    latitude = DB.Column(DB.String())
    user_id =  DB.Column(DB.Integer(), DB.ForeignKey(
        cnsts.USER_TABLE_NAME + ".id", ondelete="CASCADE"), nullable=False)
    def __init__(self, country, city, longitude, latitude, user_id):
        """
        CONSTRUCTOR
        """
        self.country = country
        self.city = city
        self.longitude = longitude
        self.latitude = latitude
        self.user_id = user_id
