import pytest


def start_prepare():
    print("\n这是一个用来执行测试之前的准备工作")


def end_operation():
    print("\n这是一个用来执行测试结束时的结束工作")


# fixture函数
@pytest.fixture()
def fixture_func():
    print("测试开始")
    # 当程序碰到yield会先执行yield前面的代码，等代码都执行完后回到yield处继续执行后面的代码
    yield start_prepare()
    end_operation()


# 测试用例
def test_1(fixture_func):
    print('测试用例1')
    assert 1 == 1


def test_2(fixture_func):
    print('测试用例2')
    assert 2 == 2
