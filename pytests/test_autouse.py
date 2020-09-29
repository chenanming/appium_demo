#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/9/29 0029 15:23
# @File: test_autouse.py
# @Poject: Appiumdemo
import pytest

@pytest.fixture(autouse="true")
def myfixture():
	print("this is my fixture")

class TestAutoUse:
	def test_one(self):
		print("执行test_one")
		assert 1 + 2 == 3

	def test_two(self):
		print("执行test_two")
		assert 1 == 1

	def test_three(self):
		print("执行test_three")
		assert 1 + 1 == 2