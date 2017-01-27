import unittest

from cppstyle import check
from cppstyle.model import parser


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.file = "tests/check_order.cpp"
        self.source = parser.parse(self.file)

    def test_force_access_specifier(self):
        # given
        root = self.source
        config = {'order': {'access_specifier_required': True}}
        # when
        result = check.check(self.file, root, config)
        # then
        expected = "[Line 5, Col 8]: Class 'Bar' should have an access specifier at first."
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), expected)

    def test_check_order(self):
        # given
        root = self.source
        config = {'order': {'access_specifier': ['public', 'protected', 'private']}}
        # when
        result = check.check(self.file, root, config)
        # then
        expected = "[Line 1, Col 0]: Class 'Foo' has wrong access specifier order: ['protected', 'public', 'private'], should be ['public', 'protected', 'private']"
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), expected)
