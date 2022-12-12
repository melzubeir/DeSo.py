"""
Unit tests for the deso.posts module.
"""
import sys
import importlib
import unittest
MODULE_PATH = "../deso/__init__.py"
MODULE_NAME = "deso"
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
from deso import Posts


class TestPosts(unittest.TestCase):
    """Test the Posts class."""

    def __init__(self, *args, **kwargs):
        super(TestPosts, self).__init__(*args, **kwargs)
        self.post_hash = '75b0244b1abc19e3e7ae0cf36f43ecb12588aa30ae48db7992edf3fb94d289ad'
        self.publicReaderKey = 'BC1YLiy1Ny1btpBkaNHBaUD5D9xX8PhdgeToPn3Fq95RhCMYQVW1Anw'

    def test_get_single_post(self):
        """Test the getSinglePost method."""
        posts = Posts()
        try:
            response = posts.getSinglePost(self.post_hash)
        finally:
            sys.stdout.write(f'\nUsing node: {posts.NODE_URL}\n')
        self.assertEqual(response.status_code, 200)

    def test_get_posts_stateless(self):
        """Test the getPostsStateless method."""
        posts = Posts(readerPublicKey=self.publicReaderKey)
        try:
            response = posts.getPostsStateless(
                postHashHex=self.post_hash,
                numToFetch=10,
            )
        except:
            raise
        finally:
            sys.stdout.write(f'\nUsing node: {posts.NODE_URL}\n')
        self.assertEqual(response.status_code, 200)

    def test_get_posts_for_public_key(self):
        """Test the getPostsForPublicKey method."""
        posts = Posts(readerPublicKey=self.publicReaderKey)
        try:
            response = posts.getPostsForPublicKey(
                publicKey=self.publicReaderKey,
            )
        except:
            raise
        self.assertEqual(response.status_code, 200)

    def test_get_diamonds_for_post(self):
        """Test the getDiamondsForPost method."""
        posts = Posts()
        try:
            response = posts.getDiamondsForPost(
                postHashHex=self.post_hash,
            )
        except:
            raise
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
