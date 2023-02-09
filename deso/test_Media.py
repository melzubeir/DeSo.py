"""
Unit tests for the deso.posts module.
"""
import unittest
import sys
from os import environ
from dotenv import load_dotenv
from deso.Media import Media


class TestMedia(unittest.TestCase):
    """Test the Media class."""

    def __init__(self, *args, **kwargs):
        super(TestMedia, self).__init__(*args, **kwargs)
        load_dotenv()
        self.publicReaderKey = environ.get('TESTBOT1_PUBKEY')
        self.media = Media()

    def test_upload_image(self):
        """Test the uploadImage method."""
        imageFileList = [
            ('file', ('deso.png', open("deso.png", "rb"), 'image/png'))
        ]
        publicKey = self.publicReaderKey
        seedHex = environ.get('TESTBOT1_SEEDHEX')
        self.media = Media(publicKey, seedHex)
        try:
            response = self.media.uploadImage(imageFileList)
        except Exception as e:
            self.fail(e)
        finally:
            sys.stdout.write(
                f'\nuploadImage() using node: {self.media.NODE_URL}\n')

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
