#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/9/29 0029 16:02
# @File: test_param.py
# @Poject: Appiumdemo
import pytest

test_user_data = ['Tome', 'Jerry']
@pytest.fixture(scope="module")
def login_r(request):
	user = request.param
	print(f"\n 登录用户：{user}")
	return user

@pytest.mark.parametrize("login_r", test_user_data,indirect=True)
def test_login(login_r):
	a = login_r
	print(f"测试用例中login的返回值: {a}")
	assert a != ""