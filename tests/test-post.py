import unittest
from app.models import Post,User,Comment

class Testpost(unittest.TestCase):
    """
    This is the class which we will use to do tests for the post
    """

    # def setUp(self):
    #     self.new_user = Post()

    # def tearDown(self):
    #     Post.query.delete()
    #     User.query.delete()
        
    def test_instance(self):
        self.assertIsInstance(self.new_post, Post)    