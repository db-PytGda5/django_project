from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..models import Post
from ..views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    about,
)


class TestUrls(SimpleTestCase):

    def test_post_list_view(self):
        url = reverse('blog-home')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_user_posts_url(self):
        url = reverse('user-posts', args=['username'])
        self.assertEquals(resolve(url).func.view_class, UserPostListView)

    def test_post_detail_url(self):
        url = reverse('post-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_post_create_url(self):
        url = reverse('post-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_post_update_url(self):
        url = reverse('post-update', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_post_delete_url(self):
        url = reverse('post-delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)

    def test_about_url(self):
        url = reverse('blog-about')
        self.assertEquals(resolve(url).func, about)