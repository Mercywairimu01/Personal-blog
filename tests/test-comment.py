import unittest
from app.models import User,Post,Comment

class TestComment(unittest.TestCase):
    """
    This is where we will run all the tests for the Comment model
    """

    def setUp(self):    
        """
        This will create a new instance of User, post and Comment before each test
        """

        self.new_user = User(name = "Premoh1")
        self.new_post = Post(title = "hello", user = self.new_user)
        self.new_comment = Comment(content = "ux", user = self.new_user, post = self.new_post)

    def tearDown(self):
        """
        Will clear the db after each test
        """
        User.query.delete()
        Post.query.delete()
        Comment.query.delete()

    def test_instance(self):
        """
        Will test whether the new comment is an instance of the Comment model
        """
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_init(self):
        """
        Will test whether the comment is instantiated correctly
        """
        self.assertEquals(self.new_comment.content, "its true")

    def test_relationship_post(self):
        """
        Will test whether the comment is correctly related to its post
        """

        post_title = self.new_comment.post.title
        self.assertTrue(post_title == "hello")

    def test_relationship_user(self):
        """
        Will test whether the comment is correctly related to the user who posted it
        """

        user_name = self.new_comment.user.name
        self.assertTrue(user_name == "Premoh1")