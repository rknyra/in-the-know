from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

#Testing the profile module
class ProfileTestClass(TestCase):
    def setUp(self):
        self.chyle=Profile(prof_pic='a771f854-c2cb-408a-8c36-71af77811f3b', bio="pilot",email='chyle@pilots.com')
        self.neighborhood=Neighborhood(location='Ontario',hood_name='GoldBeach',population=400)
        self.user=User(id=77,username='Chyle',email='chyle@pilots.com',)

    #testing the profile setUp instance
    def test_instace(self):
        self.assertTrue(isinstance(self.chyle,Profile))
    
    #testing the saving method
    def test_save_method(self):
        self.chyle.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)
    
    #tearing down the setUp profile instance
    def tearDown(self):
        Profile.objects.all().delete()
