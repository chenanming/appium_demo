import json
import pprint

class Utils:

	@classmethod
	def format(cls, json_object):
		# 方法：对数据json格式化
		return json.dumps(json_object, indent=2)