import requests

from wework_requests.api.base_api import BaseApi
from wework_requests.api.wework import WeWork


class Department(BaseApi):
	list_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'

	def list(self, id):
		res = requests.get(self.list_url, params={'access_token': WeWork.get_token(), 'id': id}).json()
		self.versobe(res)
		return res

	def create(self):
		pass

	def update(self):
		pass

	def delete(self):
		pass