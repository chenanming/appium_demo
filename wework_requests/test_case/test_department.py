from wework_requests.api.department import Department


class TestDepartment:
	department = Department()
	def setup_class(self):
		pass

	def test_list(self):
		r = self.department.list("")
		assert r["errcode"] == 0
		#assert r['department'][1]['name'] == "产品部门"

	def test_create(self):
		r = self.department.create("技术部", 1, 1000, "")
		assert r['errcode'] == 0

	def test_update(self):
		pass

	def test_delete(self):
		pass