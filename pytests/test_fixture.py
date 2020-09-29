#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/9/29 0029 13:42
# @File: test_fixture.py
# @Poject: Appiumdemo
import pytest

@pytest.fixture()
def login():
	print("这是个登录方法")
	return ('tom', '123')

@pytest.fixture()
def operate():
	print("登录后的操作")

def test_case1(login, operate):
	print(login)
	print("test_case1，需要登录")

def test_case2():
	print("test_case2，不需要登录")

def test_case3(login):
	print(login)
	print("test_case3，需要登录")