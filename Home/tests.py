import unittest
from Home.models import Home

class HomeTestCase(unittest.TestCase):
    def setUp(self):
        self.book1 = Home.objects.create(title="CCC", content="C!!")
        self.book2 = Home.objects.create(title="DDDD", content="DD!!")

    def test__unicode__(self):
        self.assertEquals(self.book1.__unicode__(), 'The lion says "roar"')
        self.assertEquals(self.book2.__unicode__(), 'The cat says "meow"')
