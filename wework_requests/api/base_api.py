from utils.Untils import Utils


class BaseApi:
	def versobe(self, json_object):
		print(Utils.format(json_object))  # 使用Utils的format()方法对json数据（r），格式化输出