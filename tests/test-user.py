import unittest
from app.models import User,Post

class TestUsers(unittest.TestCase):
    """
    This is the class which we will use to do tests for the User
    """
    def setUp(self):
        """
        This will create an instance of the User before each test case
        """

        self.new_user = User(name = "Premoh1", password = "test")

    def tearDown(self):
        """
        Will delete all the info from the db
        """
        User.query.delete()
        Post.query.delete()

    def test_instance(self):
        """
        Will test whether the new instance is an instance of the User model
        """
        self.assertTrue(isinstance(self.new_user, User))

    def test_init(self):
        """
        Will test whether the User model is instantiated correctly
        """
        self.assertEqual(self.new_user.name,"Premoh1")

    def test_save_user(self):
        """
        Will test whether the user is saved into the database
        """
        self.new_user.save_user()
        users = User.query.all()
        self.assertTrue(len(users) > 0)