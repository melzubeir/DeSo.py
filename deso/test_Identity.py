"""
Unit tests for the deso.posts module.
"""
import unittest
from os import environ
from dotenv import load_dotenv
from deso import Identity



class TestIdentity(unittest.TestCase):
    """Test the Identity class."""

    def __init__(self, *args, **kwargs):
        super(TestIdentity, self).__init__(*args, **kwargs)
        load_dotenv()
        self.jwt_token = None
        self.pubKey = environ.get('TESTBOT1_PUBKEY')
        self.seedHex = environ.get('TESTBOT1_SEEDHEX')
        self.transHex = environ.get('TESTBOT1_TANSACTIONHEX')
        self.identity = Identity(
            publicKey = self.pubKey,
            seedHex = self.seedHex,
            )

    def test_get_JWT(self):
        """Test the getJWT method."""
        self.jwt_token = self.identity.getJWT()
        self.assertIsNotNone(self.jwt_token)

    def test_validate_jwt(self):
        """Test the validateJWT method."""
        v = self.identity.validateJWT(
            JWT=self.jwt_token,
            publicKey=self.pubKey
        )
        self.assertTrue(v)

    def test_sign_transaction(self):
        """Test the signTransaction method."""
        r = self.identity.signTransaction(
            self.seedHex,
            self.transHex,
        )
        self.assertIsNotNone(r)


if __name__ == "__main__":
    unittest.main()
