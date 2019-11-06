import requests

from wework_requests.api.base_api import BaseApi
from wework_requests.api.wework import WeWork


class Department(BaseApi):
	list_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
	create_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'

	def list(self, id):
		res = requests.get(self.list_url, params={'access_token': WeWork.get_token(), 'id': id}).json()
		self.versobe(res)
		return res

	def create(self, name, parentid, order, id):
		proxies = {'http': 'http://127.0.0.1:8080/',
				   'https': 'http://127.0.0.1:8080/',
				   }
		res = requests.post(self.create_url,
							params={'access_token': WeWork.get_token()},
							json={'name': name, 'parentid': parentid, 'order': order, 'id': id},
							proxies=proxies, verify=False
							).json()
		self.versobe(res)
		return res

	def update(self):
		pass

	def delete(self):
		pass