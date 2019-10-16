import pytest

@pytest.fixture(scope="session")
def topics():
    print("\n 输入账号、密码，先登录")