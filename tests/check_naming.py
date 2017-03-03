import unittest

from cppstyle import check
from cppstyle.model import parser


class TestNaming(unittest.TestCase):
    def setUp(self):
        self.file = "tests/check_naming.cpp"
        self.source = parser.parse(self.file)

    def test_classes(self):
        # given
        config = {'naming': {'classes': '^([A-Z][a-z0-9]*)+$'}}
        # when
        result = check.check(self.file, self.source, config)
        # then
        asserted = "[Line 1, Col 0]: Class 'foo' does not match '^([A-Z][a-z0-9]*)+$'"
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), asserted)

    def test_variables(self):
        # given
        config = {'naming': {'variables': '^([a-z0-9]+)(_[a-z0-9]+)*$'}}
        # when
        result = check.check(self.file, self.source, config)
        # then
        asserted = "[Line 15, Col 2]: Variable 'wrongName' does not match '^([a-z0-9]+)(_[a-z0-9]+)*$'"
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), asserted)

    def test_private_field(self):
        # given
        config = {'naming': {'members': {'private': '^([a-z0-9]+)(_[a-z0-9]+)*_$'}}}
        # when
        result = check.check(self.file, self.source, config)
        # then
        asserted = "[Line 3, Col 8]: Field 'myPrivateString' does not match '^([a-z0-9]+)(_[a-z0-9]+)*_$'"
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), asserted)

    def test_protected_field(self):
        # given
        config = {'naming': {'members': {'protected': '^([a-z0-9]+)(_[a-z0-9]+)*_$'}}}
        # when
        result = check.check(self.file, self.source, config)
        # then
        asserted = "[Line 5, Col 8]: Field 'myProtectedString' does not match '^([a-z0-9]+)(_[a-z0-9]+)*_$'"
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), asserted)

    def test_public_field(self):
        # given
        config = {'naming': {'members': {'public': '^([a-z0-9]+)(_[a-z0-9]+)*$'}}}
        # when
        result = check.check(self.file, self.source, config)
        # then
        asserted = "[Line 7, Col 8]: Field 'myPublicString' does not match '^([a-z0-9]+)(_[a-z0-9]+)*$'"
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), asserted)

    def test_methods(self):
        # given
        config = {'naming': {'methods': '^([a-z0-9]+)([A-Z][a-z0-9]*)*$'}}
        # when
        result = check.check(self.file, self.source, config)
        # then
        asserted = ["[Line 8, Col 8]: Method 'foo_method' does not match '^([a-z0-9]+)([A-Z][a-z0-9]*)*$'"]
        self.assertEqual([str(r) for r in result],asserted)

    def test_functions(self):
        # given
        config = {'naming': {'functions': '^([a-z0-9]+)([A-Z][a-z0-9]*)*$'}}
        # when
        result = check.check(self.file, self.source, config)
        # then
        asserted = "[Line 19, Col 0]: Function 'foo_function' does not match '^([a-z0-9]+)([A-Z][a-z0-9]*)*$'"
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), asserted)


if __name__ == '__main__':
    unittest.main()
