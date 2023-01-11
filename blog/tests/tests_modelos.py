from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from ..models import Post, Comment

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        u = User.objects.create(first_name='Luis', last_name='Bob')
        p = Post.objects.create(title='My first post', 
            slug='my-first-post', 
            author=u,
            content='My first post content')
        Comment.objects.create(
            post=p, 
            name='MarÃ­a',
            email = 'maria@gmail.com',
            body = 'My first comment My first comment My first comment My first commentMy first comment'
            )

    def test_metodo_str(self):
        '''
        Comprobar que el print del objeto devuelve su tÃ­tulo
        '''
        post = Post.objects.first()
        expected_object_name = f'{post.title}'
        self.assertEquals(expected_object_name, str(post))

    def test_slug(self):
        '''
        Comprobar el slug
        '''
        post = Post.objects.first()
        slug = post.slug
        expected_slug = post.title.lower().replace(' ', '-')
        self.assertEquals(expected_slug, slug)

    def test_str_comentario(self):
        c = Comment.objects.first()
        expected_object_name = f'Comment {c.body} by {c.name}'
        self.assertEquals(expected_object_name, str(c))
        