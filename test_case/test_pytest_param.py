import pytests
import yaml
from src.clac import Clac

class TestClac:
    clac = Clac()

    @pytests.mark.parametrize("a, b, c", [
        (1, 2, 3),
        (-1, 3, 2),
        (10000, 9999, 19999),
        (-1, 0, -1)
    ])
    def test_add(self, a, b, c):
        assert self.clac.add(a, b) == c


    @pytests.mark.parametrize("a, b, c", yaml.load(open("clac.yaml")))
    def test_div(self, a, b, c):
        print(a, b, c)
        assert self.clac.div(a, b) == c