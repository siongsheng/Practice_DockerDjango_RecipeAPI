from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email='test@gmail.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating new user with an email is successful"""
        email = 'test@gmail.com'
        password = 'Password!1'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'Test123')
        
        self.assertEqual(user.email, email.lower())
        
    def test_new_user_invalid_email(self):
        """Test creating User with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')
            
    def test_create_new_useruser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'Test123'
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        
    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='vegan'
        )
        
        self.assertEqual(str(tag), tag.name)