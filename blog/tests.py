import email
from django.test import TestCase

from blog.models import *
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from accounts.models import *

class AccountsTests(TestCase):
    def setUp(self):
        self.user =get_user_model().objects.create_user(
        email='test@email.com',
        phone_number=99999,
        password='secret',
        )
        self.post = PagesModel.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        post = PagesModel(title='A sample title')
        self.assertEqual(str(post.title), post.title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'test@email.com')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_login(self):

        login=self.client.login(email='test@email.com', password='secret')
        self.assertTrue(login) 
        response = self.client.get(reverse('blog:blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'body.html')

