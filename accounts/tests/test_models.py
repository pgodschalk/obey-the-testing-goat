from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Token

User = get_user_model()


class UserModelTest(TestCase):
    def test_user_is_valid_with_email_only(self):
        user = User(email="a@example.org")
        user.full_clean()  # should not raise

    def test_email_is_primary_key(self):
        user = User(email="a@example.org")
        self.assertEqual(user.pk, "a@example.org")


class TokenModelTest(TestCase):
    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email="a@example.org")
        token2 = Token.objects.create(email="a@example.org")
        self.assertNotEqual(token1.uid, token2.uid)
