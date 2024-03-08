 
from django.test import TestCase
from django.contrib.auth.models import User

class SignupTest(TestCase):

    def test_successful_signup(self):
        """
        Tests that a user can be successfully created with valid data.
        """
        data = {
            'username': 'johndoe',
            'fname': 'John',
            'lname': 'Doe',
            'email': 'johndoe@example.com',
            'pass1': 'secretpassword',
            'pass2': 'secretpassword',
        }

        # Act
        response = self.client.post('/signup/', data=data, follow=True)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your account has been successfully created!")

        user = User.objects.get(username=data['username'])
        self.assertEqual(user.username, data['username'])
        self.assertEqual(user.first_name, data['fname'])
        self.assertEqual(user.last_name, data['lname'])
        self.assertEqual(user.email, data['email'])


def test_signup_password_mismatch(self):
    """
    Tests that signup fails when passwords do not match.
    """
    data = {
        'username': 'janedoe',
        'fname': 'Jane',
        'lname': 'Doe',
        'email': 'janedoe@example.com',
        'pass1': 'differentpassword',
        'pass2': 'anotherpassword',
    }

    response = self.client.post('/signup/', data=data, follow=True)

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Passwords do not match.")
    self.assertEqual(User.objects.count(), 0)  # No user should be created


def test_signup_existing_username(self):
    """
    Tests that signup fails when the username already exists.
    """
    # Create a user object beforehand (simulating an existing user)
    existing_user = User.objects.create_user(username='existinguser', password='existingpassword')

    data = {
        'username': 'existinguser',  # Using the existing username
        'fname': 'Existing',
        'lname': 'User',
        'email': 'existing@example.com',
        'pass1': 'somepassword',
        'pass2': 'somepassword',
    }

    response = self.client.post('/signup/', data=data, follow=True)

    self.assertEqual(response.status_code, 200)
    # Django's default behavior might display a generic error message
    self.assertContains(response, "A user with that username already exists.")
    self.assertEqual(User.objects.count(), 1)  # Existing user remains

    # Clean up: delete the created user
    existing_user.delete()
#-------------------------------------------------------------------------------------------------#
    import unittest
from django.test import Client
from django.contrib.auth.models import User
from mytown.views import signup

class SignupTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_success(self):
        response = self.client.post('/signup/', {
            'username': 'testuser',
            'fname': 'Test',
            'lname': 'User',
            'email': 'test@example.com',
            'pass1': 'testpassword',
            'pass2': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to signin upon successful signup

        # Check if user is created
        user = User.objects.get(username='testuser')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.email, 'test@example.com')
