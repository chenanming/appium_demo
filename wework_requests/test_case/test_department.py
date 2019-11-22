# _*_ coding:utf-8 _*_

from wework_requests.api.department import Department


class TestDepartment:
	department = Department()
	department_list = []

	def setup_class(self):
		pass

	def test_list(self):
		r = self.department.list()
		assert r["errcode"] == 0
		assert r['department'][1]['name'] == "产品部门"

	def test_create(self):
		r = self.department.create("编辑部", 1)
		assert r['errcode'] == 0
		assert r['id'] != 0

		# 方法二：
		exist = False
		for depar in self.department.list()['department']:
			if depar['id'] == r['id']:
				exist = True
		assert exist == True

		'''
		# 方法一：判断：当errcode = 0 时，遍历响应数据的department的value，取出所有的key="name"的value，存到department_list
		if r['errcode'] == 0:
			r = self.department.list()
			department = r['department']
			for item in department:
				for key in item.keys():
					if key == 'name':
						self.department_list.append(item[key])
			print(self.department_list)
			assert "编辑部" in self.department_list  # 验证department_list，是否有刚创建的“部门名称”
		'''

	def test_update(self):
		pass

	def test_delete(self):
		r = self.department.delete(5)
		assert  r['errcode']  == 0

		exist = False
		for depar in self.department.list()['department']:
			if depar['id'] != 5:
				exist = True
		assert exist == True