import unittest
from cppstyle import check_order,utils

class TestNaming(unittest.TestCase):

    def parse_source(self):
        import clang.cindex as ci
        index = ci.Index.create()
        source = index.parse("tests/check_order.cpp")
        return source.cursor

    def test_force_access_specifier(self):
        # given
        root = self.parse_source()
        config = { 'order': {'access_specifier_required': "True" }}
        # when
        result = check_order.check(root,config)
        # then
        expected = "[Line 5, Col 15]: Class 'Bar' should have an access specifier at first."
        self.assertEqual(len(result),1)
        self.assertEqual(str(result[0]),expected)

    def test_check_specifier(self):
        # given
        root = self.parse_source()
        config = { 'order': {'access_specifier': [ 'public', 'protected', 'private']} }
        # when
        result = check_order.check(root,config)
        # then
        expected = "[Line 1, Col 7]: Class 'Foo' has wrong access specifier order: ['protected', 'public', 'private'], should be ['public', 'protected', 'private']"
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), expected)

    def test_order(self):
        root = self.parse_source()
