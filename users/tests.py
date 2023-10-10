from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User

class UserRegistrationAPIViewTestCase(APITestCase):
    def test_registration(self):
        url = reverse('user_view')
        user_data = {
            "username": "jisutester",
            "fullname": "jisutester",
            "email": "k@k.com",
            "password": "1234",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 200)


    def test_login(self):
        url = reverse('token_obtain_pair')
        user_data = {
            "username": "jisutester",
            "fullname": "jisutester",
            "email": "k@k.com",
            "password": "1234",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 200)


class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {'username':'jisutester','password':'jisupassword'}
        self.user = User.objects.create_user('john','jisupassword')

    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'),self.data)
        self.assertEqual(response.status_code, 200)

    def test_get_user_data(self):
        access_token = self.client.post(reverse('token_obtain_pair'),self.data).data['access']
        response = self.client.get(
            path = reverse("user_view"),
            HTTP_AUTHORIZATION = 'Bearer {access_token}'
            )
        print(response.data)
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.data['username'], self.data['username'])