# _*_ coding:utf-8 _*_

import requests
import logging
logging.basicConfig(
    level=logging.INFO
)

from wework_requests.api.base_api import BaseApi


class WeWork(BaseApi):
	corpid = 'wwda2949fda2df78ef'  # 企业ID
	agent_secret = 'Ci-POCmt0gJg_q-v6-sSROV0wc9hms_EU791KNcNU_Q'  # 应用secret
	cont_secret = 'nfwiyl5yV7Nu7xrT6OytyRlDuNNhoZQcdoJJ_nA49_0'  # 通讯录secret
	access_token = None

	@classmethod
	def get_token(cls):
		# 缓存access_token，先定义一个空值变量
		if cls.access_token==None:
			url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
			params = {'corpid': cls.corpid, 'corpsecret': cls.cont_secret}
			res = requests.get(url, params=params).json()
			cls.versobe(res)
			# self.access_token = res['access_token']  # 具体的实例
			cls.access_token = res['access_token']  # WeWork类的实例，供全局调用

		return WeWork.access_token

if __name__ == "__main__":
	we = WeWork()
	we.get_token()
	print(we.access_token)