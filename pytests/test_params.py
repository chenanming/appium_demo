#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/9/29 0029 15:31
# @File: test_params.py
# @Poject: Appiumdemo
import pytest

@pytest.fixture(params=[1,2,3])
def data(request):
	return request.param

def test_not_2(data):
	print(f"测试数据：{data}")
	assert data < 5