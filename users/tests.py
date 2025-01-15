from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser


class CustomUserModelTests(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)

    def test_create_user(self):
        """Test creating a new user with email"""
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertEqual(self.user.username, self.user_data['username'])
        self.assertTrue(self.user.check_password(self.user_data['password']))
        self.assertFalse(self.user.is_staff)
        self.assertTrue(self.user.is_active)

    def test_user_string_representation(self):
        """Test the string representation of user"""
        self.assertEqual(str(self.user), self.user_data['email'])


class CustomUserCreationFormTests(TestCase):
    def setUp(self):
        self.valid_form_data = {
            'email': 'newuser@example.com',
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'user_type': '0'
        }

    def test_valid_user_form(self):
        """Test form with valid data"""
        form = CustomUserCreationForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_duplicate_email(self):
        """Test form validation for duplicate email"""
        CustomUser.objects.create_user(
            email='newuser@example.com',
            username='existinguser',
            password='testpass123'
        )
        form = CustomUserCreationForm(data=self.valid_form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_duplicate_username(self):
        """Test form validation for duplicate username"""
        CustomUser.objects.create_user(
            email='different@example.com',
            username='newuser',
            password='testpass123'
        )
        form = CustomUserCreationForm(data=self.valid_form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_password_mismatch(self):
        """Test form validation for password mismatch"""
        self.valid_form_data['password2'] = 'wrongpass'
        form = CustomUserCreationForm(data=self.valid_form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)


class CustomAuthenticationFormTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpass123',
            is_staff=True
        )
        self.client = Client()

    def test_valid_authentication(self):
        """Test authentication with valid credentials"""
        form = CustomAuthenticationForm(data={
            'username': 'test@example.com',
            'password': 'testpass123'
        })
        self.assertTrue(form.is_valid())

    def test_inactive_user(self):
        """Test authentication with inactive user"""
        self.user.is_active = False
        self.user.save()
        form = CustomAuthenticationForm(data={
            'username': 'test@example.com',
            'password': 'testpass123'
        })
        self.assertFalse(form.is_valid())

    def test_non_staff_user(self):
        """Test authentication with non-staff user"""
        self.user.is_staff = False
        self.user.save()
        form = CustomAuthenticationForm(data={
            'username': 'test@example.com',
            'password': 'testpass123'
        })
        self.assertFalse(form.is_valid())


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')

        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpass123',
            is_staff=True
        )

    def test_register_view_GET(self):
        """Test GET request to register view"""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)

    def test_register_view_POST_valid(self):
        """Test POST request to register view with valid data"""
        response = self.client.post(self.register_url, {
            'email': 'newuser@example.com',
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'user_type': '1'
        })
        self.assertRedirects(response, self.login_url)
        self.assertTrue(
            CustomUser.objects.filter(email='newuser@example.com').exists()
        )

    def test_login_view_GET(self):
        """Test GET request to login view"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_view_POST_valid(self):
        """Test POST request to login view with valid credentials"""
        response = self.client.post(self.login_url, {
            'username': 'test@example.com',
            'password': 'testpass123'
        })
        self.assertRedirects(response, self.home_url)

    def test_login_view_POST_invalid(self):
        """Test POST request to login view with invalid credentials"""
        response = self.client.post(self.login_url, {
            'username': 'test@example.com',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logout_view(self):
        """Test logout functionality"""
        self.client.login(username='test@example.com', password='testpass123')
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.login_url)

    def test_authenticated_user_redirect(self):
        """Test that authenticated users are redirected from login/register pages"""
        self.client.login(username='test@example.com', password='testpass123')
        response = self.client.get(self.login_url)
        self.assertRedirects(response, self.home_url)

        response = self.client.get(self.register_url)
        self.assertRedirects(response, self.home_url)