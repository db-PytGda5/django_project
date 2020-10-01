from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from ..models import Post


class TestViews(TestCase):

    def setUp(self):
        Post.objects.create(
            title='testtitle',
            content='testcontent',
            date_posted=timezone.now(),
            author=User.objects.create(username='testuser')
        )

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_about_page_status(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'testtitle')
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_user_post_list_view(self):
        response = self.client.get(reverse('user-posts', args=['testuser']))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertTemplateUsed(response, 'blog/user_posts.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post-detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'testtitle')
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_create_view(self):
        response = self.client.get(reverse('post-create'))
        self.assertEquals(response.status_code, 302)

    def test_post_update_view(self):
        response = self.client.get(reverse('post-update', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.get(reverse('post-delete', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 302)
