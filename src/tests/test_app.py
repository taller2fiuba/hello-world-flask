import unittest
import mock

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    @mock.patch('app.requests.get')
    def test_root_text(self, mock_get):
        mock_get.return_value.json = lambda: {'title': "Hello world!"}
        response = self.app.get('/')
        self.assertEqual(response.json, {'title': f'(Hello world!) by Flask'})


if __name__ == '__main__':
    unittest.main()
