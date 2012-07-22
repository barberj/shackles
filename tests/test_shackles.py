from unittest import TestCase
import shackles

class prisoner(object):
    """Dummy object to shackle to for testing"""
    def __init__(self, name=None):
        self.name = name

class test_shackles(TestCase):

    def setUp(self):
        self.obj = prisoner()
        self.obj.a = prisoner('a')
        self.obj.a.b = prisoner('b')
        self.obj.a.b.e = prisoner('e')

    def test_broken_chain_str(self):
        assert shackles.broken(self.obj, 'e') is 'e'
        assert shackles.broken(self.obj, 'a.b') is None
        assert shackles.broken(self.obj, 'a.b.c') == 'c'

    def test_broken_chain_list(self):
        assert shackles.broken(self.obj, ['e']) is 'e'
        assert shackles.broken(self.obj, ['a','b']) is None
        assert shackles.broken(self.obj, ['a','b','c']) == 'c'

    def test_broken_chain_tuple(self):
        assert shackles.broken(self.obj, ('e')) is 'e'
        assert shackles.broken(self.obj, ('a','b')) is None
        assert shackles.broken(self.obj, ('a','b','c')) == 'c'

    def test_get_str(self):
        assert shackles.get(self.obj, 'a.b').name == 'b'
        assert shackles.get(self.obj, 'a.b.name') == 'b'

    def test_get_list(self):
        assert shackles.get(self.obj, ['a','b']).name == 'b'
        assert shackles.get(self.obj, ['a','b','name']) == 'b'

    def test_get_tuple(self):
        assert shackles.get(self.obj, ('a','b')).name == 'b'
        assert shackles.get(self.obj, ('a','b','name')) == 'b'
