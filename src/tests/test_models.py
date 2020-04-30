import unittest
import mock

from app.models import User


class ModelTestCase(unittest.TestCase):

    def test_user_repr(self):
        u = User(username='Lucho', email='lucho@lucho.lucho')
        self.assertEqual(repr(u), '<User Lucho>')


