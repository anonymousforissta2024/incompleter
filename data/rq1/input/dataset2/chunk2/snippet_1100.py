#Source: https://stackoverflow.com/questions/31284240/typeerror-type-str-doesnt-support-the-buffer-api-in-asserttrue-in-testcase
from django.test import TestCase
from .models import Artists

class TestArtist(TestCase):
    def setUp(self):
        self.artist = Artists.objects.create(first_name = 'Ricky', 
        last_name ='Martin')

    def test_existe_vista(self):
        #print (self.client.get('/artists/%d' % self.artist.id))
        res = self.client.get('/artists/%d' % self.artist.id)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('Ricky' in res.content)