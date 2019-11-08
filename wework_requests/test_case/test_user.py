#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/11/7 0007 14:23
# @File: test_user.py
# @Poject: Appiumdemo

from wework_requests.api.user import User

class TestUser:
	user = User()
	def setup_class(self):
		pass

	def test_simplelist(self):
		r = self.user.simplelist(1)
		assert r['errcode'] == 0

	def test_create(self):
		r = self.user.create("011", "刘艺", 3, "老刘", "13133832759")
		assert r['errcode'] == 0

	def test_get(self):
		pass

	def test_update(self):
		pass

	def test_delete(self):
		pass

	def test_batchdelete(self):
		pass

	def test_list(self):
		pass
