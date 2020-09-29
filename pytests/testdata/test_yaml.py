#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/9/29 0029 16:26
# @File: test_yaml.py
# @Poject: Appiumdemo
import pytest
import yaml

@pytest.mark.parametrize("a,b",yaml.safe_load(open("data.yml", encoding='utf-8')))
def test_foo(a,b):
	print(f"a + b = {a + b}")