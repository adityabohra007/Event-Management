from django.test import TestCase

# Create your tests here.
class TestIndex(TestCase):
    def test_render_for_all(self):
        response = self.client.get('/anything/')
        self.assertEquals(response.status_code,200)