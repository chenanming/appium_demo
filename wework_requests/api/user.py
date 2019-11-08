#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/11/7 13:13
# @File: user.py
# @Poject: Appiumdemo
import requests

from wework_requests.api.base_api import BaseApi
from wework_requests.api.wework import WeWork


class User(BaseApi):
	simelelist_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist'
	create_url = 'https://wx66eaeb090ad01ef1.youshuge.com/jump_recharge_act?activity_id='

	def simplelist(self, department_id, id=None):
		# 获取部门成员
		res = requests.get(self.simelelist_url, params={'access_token': WeWork.get_token(), 'department_id': department_id, 'id': id}).json()
		self.versobe(res)
		return res

	def create(self, userid, name, department, alias=None, mobile=None):
		# 创建成员
		data = {
			"userid": userid,  # <True> 成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母
			"name": name,  # <True> 成员名称。长度为1~64个utf8字符
			"alias": alias,  # <False> 成员名称。长度为1~64个utf8字符
			"mobile": mobile,  # <False> 手机号码。企业内必须唯一，mobile/email二者不能同时为空
			"department": department  # <True> 成员所属部门id列表,不超过20个
		}
		res = requests.get(self.create_url, params={'access_token': WeWork.get_token(),
													'userid': userid, 'name': name, 'alias': alias, 'mobile': mobile, 'department': department}).json()
		self.versobe(res)
		return res

	def get(self):
		# 读取成员
		pass

	def update(self):
		# 更新成员
		pass

	def delete(self):
		# 删除成员
		pass

	def batchdelete(self):
		# 批量删除成员
		pass

	def list(self):
		# 获取部门成员详情
		pass