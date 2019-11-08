# _*_ coding:utf-8 _*_

import requests

from wework_requests.api.base_api import BaseApi
from wework_requests.api.wework import WeWork


class Department(BaseApi):
	list_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
	create_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
	delete_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
	headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}

	def list(self, id=None):
		res = requests.get(self.list_url, params={'access_token': WeWork.get_token(), 'id': id}).json()
		self.versobe(res)  # 打印响应数据
		return res

	def create(self, name, parentid, order=None, id=None):
		'''
		:param name: <True>部门名称。长度限制为1~32个字符，字符不能包括\:?”<>｜
		:param parentid: <True>父部门id，32位整型
		:param order: <False>在父部门中的次序值。order值大的排序靠前。有效的值范围是[0, 2^32)
		:param id: <False>在父部门中的次序值。order值大的排序靠前。有效的值范围是[0, 2^32)
		:return:
		'''

		proxies = {'http': 'http://127.0.0.1:8080/',
				   'https': 'http://127.0.0.1:8080/',
				   }
		res = requests.post(self.create_url,
							params={'access_token': WeWork.get_token()},
							json={"name": name, "parentid": parentid, "order": order, "id": id},
							#proxies=proxies,  # 映射指定的代理的url
							verify=False
							).json()
		self.versobe(res)  # 打印响应数据
		return res

	def update(self):
		pass

	def delete(self, id=None):
		res = requests.get(self.delete_url, params={'access_token': WeWork.get_token(), 'id': id}).json()
		self.versobe(res)  # 打印响应数据
		return res