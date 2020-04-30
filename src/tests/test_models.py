import unittest

from app.models import User


class ModelTestCase(unittest.TestCase):
    def test_user_repr(self):
        user = User(username='Lucho', email='lucho@lucho.lucho')
        self.assertEqual(repr(user), '<User Lucho>')
