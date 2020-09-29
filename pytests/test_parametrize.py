#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/9/29 0029 15:45
# @File: test_parametrize.py
# @Poject: Appiumdemo
import pytest

@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+5", 7), ("7*5", 35)])
def test_eval(test_input,expected):
	#eval将字符串str当作有效的表达式来求值，并返回结果
	assert eval(test_input) == expected

@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[8,10,12])
def test_foo(x,y):
	print(f"测试数据组合x：{x}, y:{y}")