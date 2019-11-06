from wework_requests.api.department import Department


class TestDepartment:
	def test_list(self):
		departemt = Department()
		r = departemt.list("")
		assert r["errcode"] == 0
		#assert r['department'][1]['name'] == "产品部门"

	def test_create(self):
		pass

	def test_update(self):
		pass

	def test_delete(self):
		pass