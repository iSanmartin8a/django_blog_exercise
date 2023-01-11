from django.test import TestCase

from django.contrib.auth.models import User
from blog.models import Post

# Create your tests here.
class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        u = User.objects.create(first_name='Angela', last_name='Malfoy')
        p = Post.objects.create(title='My first post', slug='my-first-post', author=u, content='This is my first post content', status=2)

    def test_object_name_is_last_name_comma_first_name(self):
        '''
        Comprobar que el print del objeto devuelve el título
        '''
        post = Post.objects.first()
        expected_object_name = f'{post.title}'
        self.assertEquals(expected_object_name, str(post))

    def test_slug(self):
        '''
        Comprobar que el slug se genera correctamente
        '''
        post = Post.objects.first()
        slug = post.slug
        expected_slug = post.title.lower().replace(' ', '-')
        self.assertEquals(expected_slug, slug)