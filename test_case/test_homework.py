import logging
import pytest
import allure
import pytest_ordering

logging.basicConfig(level=logging.DEBUG)

def setup_module():
    logging.info("login")
def teardown_module():
    logging.info("执行数据清理")

class TestA:
    @allure.feature("test_01")
    def test_01(self):
        '''测试判断'''
        assert 1 == 1
    def test_02(self):
        assert 1 == 1
    def test_03(self):
        assert -1 != 1

    @classmethod
    def teardown_class(cls):
        logging.info("   TestA 完成环境清理")


class TestB:

    def setup_method(self):
        logging.info("   TestB 中每个用例方法，初始化")

    @pytest.mark.parametrize("a, b, c", [
        (1, 2, 3),
        (-1, 3, 2),
        (10000, 9999, 19999),
        (-1, 0, -1)
    ])
    def test_04(self, a, b, c):
        assert a+b == c

    @pytest.mark.parametrize("a, b, c", [
        (3, 1, 3)
    ])
    def test_05(self, a, b, c):
        assert a/b == c

    @pytest.mark.parametrize("a, b", [
        (1, 3),
        (1, 2),
        (3, 5)
    ])
    def test_06(self, a, b):
        assert a != b


class TestC:

    @pytest.mark.run(order=-1)
    def test_07(self):
        assert 1 == 1

    @pytest.mark.run(order=-3)
    def test_08(self):
        assert 2 != 3

    @pytest.mark.run(order=-2)
    def test_09(self):
        assert  3 == 3

if __name__ == '__main__':
    pytest.main()