import json
import pprint

class Utils:

	@classmethod
	def format(cls, json_object):
		# ������������json��ʽ��
		return json.dumps(json_object, indent=2)