from unittest import TestCase
from utils.Untils import Utils


class TestUtils(TestCase):
	def test_format(self):
		json = Utils.format({'errcode':0, 'data': {'a': '1', 'b':[{'c':2, 'd':3}]}})
		print(json)
