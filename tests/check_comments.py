import unittest

from cppstyle.model import parser


class TestComments(unittest.TestCase):
    def setUp(self):
        self.header = "tests/check_comments.hpp"
        self.header_source = parser.parse(self.header)
        self.impl = "tests/check_comments.cpp"
        self.impl_source = parser.parse(self.impl)

    def test(self):
        self.assertEquals(0, 0)
