# -*- conding:utf-8 -*-
'''
以PO模式完成如下功能的业务测试

通讯录Page 新增
搜索结果页Profile 编辑 禁用 启动
管理工具Page goto添加图片
图片管理Page 添加图片
封装出完整的PO，把代码上传到github并贴项目git地址到回复里
'''

from time import sleep, time
import pytest, allure
from selenium import webdriver
from test_po.contact_page import ContactPage
from test_po.base_page import BaseDriver
from test_po.profile_page import ProfilePage
from test_po.wework_page import Wework
from test_po.manage_tool_page import ManageToolPage
from selenium.webdriver.common.by import By

@allure.feature("第十期_Selenium PO 与企业微信实战_20190804 课后作业")
class TestContact:
    _tips = (By.CSS_SELECTOR, ".js_tips")  # 提示

    def setup(self):
        self.work = Wework()
        self.contact = ContactPage(self.work.driver)
        self.manage = ManageToolPage(self.work.driver)

    def teardown(self):
        sleep(10)
        self.contact.driver.quit()

    @allure.story("通讯录，添加成员")
    def test_add_member(self):
        self.contact.add_member("test02", "003", "13133832893")

    #def test_add_member_chinese(self):
    #    self.contact.add_member("安明", "002", "13133832791")
    #    assert self.contact.get_title_page() == "ok"

    #def test_delete(self):
    #    udid=str(time())
    #    self.contact.add_member("安明"+udid, "002"+udid, "13133832791")

    @allure.story("搜索结果页Profile 编辑成员信息")
    def test_update_profile(self):
        self.contact.search("test02").update(name="tester %s" % str(time()))

    @allure.story("管理工具Page goto添加图片")
    def test_add_picture(self):
        self.manage.add_picture()

if __name__ == '__main__':
    pytest.main()