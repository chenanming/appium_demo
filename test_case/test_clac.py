from unittest import TestCase

from ddt import ddt, data, unpack, file_data

from src.clac import Clac

@ddt
class TestClac(TestCase):
    def setUp(self) -> None:
        self.clac = Clac()

    @data((2, 1, 2),
        (-3, 1, -3),
        (0, 2, 0),
        (10000, 10, 1000))
    @unpack
    def test_div(self, a, b, c):
        assert (self.clac.div(a, b) == c)


    @file_data("clac.yaml")
    def test_add(self, a, b, c):
        assert (self.clac.add(a, b) == c)