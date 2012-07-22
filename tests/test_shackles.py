from unittest import TestCase
import shackles

class prisoner(object):
    """Dummy object to shackle to for testing"""
    pass

class test_shackles(TestCase):

    def setUp(self):
        self.obj = prisoner()
        self.obj.a = prisoner()
        self.obj.a.b = prisoner()

    def test_broken_chain_str(self):

        assert shackles.broken(self.obj, 'a.b') is None
        assert shackles.broken(self.obj, 'a.b.c') == 'c'

    def test_broken_chain_list(self):

        assert shackles.broken(self.obj, ['a','b']) is None
        assert shackles.broken(self.obj, ['a','b','c']) == 'c'

    def test_broken_chain_tuple(self):

        assert shackles.broken(self.obj, ('a','b')) is None
        assert shackles.broken(self.obj, ('a','b','c')) == 'c'
