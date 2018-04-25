from flask_testing import TestCase

from learning.database.user_model import UserModel
from learning.application import APP
from learning.configuration import configure_api
from learning.application_vars import DB


class BaseTest(TestCase):
    def create_app(self):
        APP.config.from_object('learning.configuration.TestingConfig')
        configure_api()
        return APP
    
    def setUp(self):
        DB.session.add(UserModel('rohit','negi','rohit.negi@gmail.com','1234'))
        DB.create_all()

    
    def tearDown(self):
        DB.session.remove()
        DB.drop_all()



class TestRegister(BaseTest):

    def test_ideal_lgon(self):
      
        response = self.client.post('/login',data={'email':'rohit.negi@gmail.com','password':'1234'})
        self.assertTrue(response.status_code==200)
        self.assertTrue('access_token' in response.json)

