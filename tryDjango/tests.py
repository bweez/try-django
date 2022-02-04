from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password


class tryDjangoConfigTest(TestCase):
    # https://docs.python.org/3/library/unittest.html
    def test_secret_key(self):

        # Another option
        # import os
        # SECRET_KEY = os.environ.get('SECRET_KEY')
        SECRET_KEY = settings.SECRET_KEY
        self.assertIsNotNone(SECRET_KEY)
        try:
            validate_password(SECRET_KEY)
        except Exception as e:
            self.fail(f'Weak Secret Key - {e.message}')
