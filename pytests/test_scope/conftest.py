#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/9/29 0029 15:09
# @File: conftest.py
# @Poject: Appiumdemo
import pytest

@pytest.fixture(scope="session")
def open():
	print("打开浏览器")
	yield

	print("执行teardown ！")
	print("最后关闭浏览器")