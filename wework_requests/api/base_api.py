from utils.Untils import Utils
import pprint

class BaseApi:
	printer=pprint.PrettyPrinter(indent=2)

	@classmethod
	def versobe(cls, json_object):
		print(Utils.format(json_object))  # ʹ��Utils��format()������json���ݣ�r������ʽ�����
		#cls.printer.pprint(json_object)  # ʹ��pprint������ʽ����