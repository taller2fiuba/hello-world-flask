from app import app

import unittest

class AppTestCase(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_root_text(self):
        response = self.app.get('/')
        self.assertEqual(response.data, "Hello world!")

if __name__ == '__main__':
    unittest.main()
