from django.test import TestCase, Client
from django.utils import timezone as tz
from django.urls import reverse

from blog.models import Post, Comment
n = 0

class ViewTestCase(TestCase):
    fixtures = ['dump.json']

    def setUp(self):
        self.client = Client()
        self.last_post = Post.objects.filter(modified_date__lte=tz.now()).order_by('-modified_date')[0]

        global n
        print(n, self.last_post)
        n+=1

    def test_index(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('first_row_reciepts' in resp.context)
        self.assertContains(resp, self.last_post.title.title(), html=True)

    def test_list_of_reciepts_for_2019(self):
        resp = self.client.get('/reciepts/year/2019')
        self.assertEqual(resp.status_code, 200)