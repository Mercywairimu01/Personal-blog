import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

     def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
    