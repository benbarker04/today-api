from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='ben', password='pass')

    def test_can_list_posts(self):
        ben = User.objects.get(username='ben')
        Post.objects.create(owner=ben, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_make_post(self):
        self.client.login(username='ben', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_make_post(self):
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class PostDetailViewTests(APITestCase):
    def setUp(self):
        ben = User.objects.create_user(username='ben', password='pass')
        charlie = User.objects.create_user(username='charlie', password='pass')
        Post.objects.create(
            owner=ben, title='a title', content='bens content'
        )
        Post.objects.create(
            owner=charlie, title='another title', content='charlies content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/5')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def  test_user_can_update_own_post(self):
        self.client.login(username='ben', password='pass')
        response = self.client.put('/posts/1', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_other_users_post(self):
        self.client.login(username='ben', password='pass')
        response = self.client.put('/posts/2', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)