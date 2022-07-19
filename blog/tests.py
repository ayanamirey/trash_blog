from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Comment


class PostTests(APITestCase):
    def setUp(self):
        Post.objects.create(title='Дора', text='Дора контент')
        # Women.objects.create(title='Бейонсе', content='Бейонсе контент')

    def test_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

