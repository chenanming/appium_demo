from utils.Untils import Utils
import pprint

class BaseApi:
	printer=pprint.PrettyPrinter(indent=2)

	@classmethod
	def versobe(cls, json_object):
		print(Utils.format(json_object))  # 使用Utils的format()方法对json数据（r），格式化输出
		#cls.printer.pprint(json_object)  # 使用pprint方法格式数据