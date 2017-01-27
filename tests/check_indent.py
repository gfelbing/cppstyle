import unittest

from cppstyle import check
from cppstyle.model import parser


class TestIndent(unittest.TestCase):
    def setUp(self):
        self.file = "tests/check_indent.cpp"
        self.source = parser.parse(self.file)

    def test_function(self):
        # given
        config = {'indent': {'function': 2}}
        # when
        result = check.check(self.file, self.source, config)
        # then
        asserted = "[Line 3, Col 4]: Indent is wrong, should be '2', not '4'"
        # self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), asserted)

    def test_method(self):
        # given
        config = {'indent': {'method': 2}}
        # when
        result = check.check(self.file, self.source, config)
        # then
        asserted = "[Line 14, Col 6]: Indent is wrong, should be '4', not '6'"
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), asserted)

    def test_struct(self):
        # given
        config = {'indent': {'struct': 2}}
        # when
        result = check.check(self.file, self.source, config)
        # then
        asserted = "[Line 9, Col 8]: Indent is wrong, should be '6', not '8'"
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), asserted)

    def test_class(self):
        # given
        config = {'indent': {'class': {'access_specifier': 0, 'default': 2}}}
        # when
        result = check.check(self.file, self.source, config)
        # then
        asserted = [
            "[Line 7, Col 1]: Indent is wrong, should be '0', not '1'",
            "[Line 8, Col 4]: Indent is wrong, should be '2', not '4'"
        ]
        self.assertEqual(len(result), 2)
        self.assertEqual(asserted, [str(r) for r in result])
