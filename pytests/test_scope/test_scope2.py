#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/9/29 0029 15:10
# @File: test_scope2.py
# @Poject: Appiumdemo
import pytest

class TestFunc():
	def test_case1(self):
		print("test_case1，需要登录")

	def test_case2(self):
		print("test_case2，不需要登录")

	def test_case3(self):
		print("test_case3，需要登录")