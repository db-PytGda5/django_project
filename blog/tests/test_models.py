from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from ..models import Post


class TestModel(TestCase):

    def setUp(self):
        Post.objects.create(
            title='testtitle',
            content='testcontent',
            date_posted=timezone.now(),
            author=User.objects.create(username='testuser')
            )

    def test_post(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.title, 'testtitle')
        self.assertEquals(str(post), 'testtitle')