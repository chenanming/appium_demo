import requests
import logging
logging.basicConfig(
    level=logging.INFO
)


class WeWork:
	corpid = 'wwda2949fda2df78ef'  # ��ҵID
	agent_secret = 'Ci-POCmt0gJg_q-v6-sSROV0wc9hms_EU791KNcNU_Q'  # Ӧ��secret
	cont_secret = 'nfwiyl5yV7Nu7xrT6OytyRlDuNNhoZQcdoJJ_nA49_0'  # ͨѶ¼secret
	access_token = None

	@classmethod
	def get_token(cls):
		# ����access_token���ȶ���һ����ֵ����
		if cls.access_token==None:
			url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
			params = {'corpid': cls.corpid, 'corpsecret': cls.cont_secret}
			res = requests.get(url, params=params).json()
			print(res)
			# self.access_token = res['access_token']  # �����ʵ��
			cls.access_token = res['access_token']  # WeWork���ʵ������ȫ�ֵ���

		return WeWork.access_token