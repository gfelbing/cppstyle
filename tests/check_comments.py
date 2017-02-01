import unittest

from cppstyle import check
from cppstyle.model import parser


class TestComments(unittest.TestCase):
    def setUp(self):
        self.header = "tests/check_comments.hpp"
        self.header_source = parser.parse(self.header)

    def test_classes(self):
        # given
        config = {"comments": {"class": {
            "default": "^((?:.|\n)+)$",
            "brief": "^((?:.|\n){0,80})$"
        }}}

        # when
        issues = check.check(self.header, self.header_source, config)

        # then
        asserted = [
            "[Line 10, Col 0]: Comment 'This is a brief description of Foo. It is good that is\nhas a brief comment, but it is way to long. In our test it should be 80 chars at max.' does not match '^((?:.|\n){0,80})$'",
            '[Line 22, Col 0]: Missing a default comment.'
        ]
        self.assertEqual([str(i) for i in issues], asserted)

    def test_parameter(self):
        # given
        config = {"comments": {"parameter": "^((?:.|\n){0,20})$"}}

        # when
        issues = check.check(self.header, self.header_source, config)

        # then
        asserted = [
            "[Line 16, Col 24]: Parameter 'fooBar' is missing a comment.",
            "[Line 16, Col 4]: Parameter comment 'foo is a parameter with a too long description.' does not match '^((?:.|\n){0,20})$'"
        ]
        self.assertEqual([str(i) for i in issues], asserted)
