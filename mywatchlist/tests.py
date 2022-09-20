from django.test import TestCase

# Create your tests here.
class StatusCodeTestCase(TestCase):
    def test_ok_html(self):
        response = self.client.get('/mywatchlist/html', follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_ok_xml(self):
        response = self.client.get('/mywatchlist/xml', follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_ok_json(self):
        response = self.client.get('/mywatchlist/json', follow=True)
        self.assertEqual(response.status_code, 200)