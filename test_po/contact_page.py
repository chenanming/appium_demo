# conding=utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_po.wework_page import Wework
from test_po.base_page import BaseDriver
from test_po.profile_page import ProfilePage


class ContactPage(BaseDriver):
    _address_list=(By.CSS_SELECTOR, "#menu_contacts > span")        # 通讯录
    _invite=(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")    # 邀请
    _username=(By.ID, "username")                                   # 姓名
    _alias=(By.NAME, "acctid")                                      # 账号
    _phone=(By.ID, "memberAdd_phone")                               # 手机号
    _search=(By.ID, "memberSearchInput")                            # 搜索框
    _save=(By.LINK_TEXT, "保存")                                    # 编辑、保存按钮



    def add_member(self, name, id, mobile, **kwargs):
        self.driver.find_element(*self._address_list).click()       # 点击 通讯录
        self.driver.find_element(*self._invite).click()             # 点击邀请成员
        WebDriverWait(self.driver, 10, 0.5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".js_add_member")))
        self.driver.find_element(*self._username).send_keys(name)    # 输入姓名
        self.driver.find_element(*self._alias).send_keys(id)        # 输入账号
        self.driver.find_element(*self._phone).send_keys(mobile)     # 输入手机号
        self.driver.find_element(*self._save).click()                # 点击保存按钮
        return self

    def delete_member(self):
        pass


    def search(self, key):
        self.driver.find_element(*self._search).send_keys(key)
        return ProfilePage(self.driver)
