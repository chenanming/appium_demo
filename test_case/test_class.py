import yaml
import pytest
from src.clac import Clac

clac = Clac()
# 读取yaml文件
def load_json():
    with open('clac.yaml', 'r') as f:
        re = yaml.load(f)
    return re

@pytest.mark.parametrize("a, b, c", str(load_json()))
def test_div(a, b, c):
    assert a/b == c