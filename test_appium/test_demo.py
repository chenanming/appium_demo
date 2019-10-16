# -*- coding: utf-8 -*-
# @Time    :2019/8/16
# @Author  :陈安明
# @File    :
import pytest
import allure
from appium import webdriver
from selenium.webdriver.common.by import By


@allure.feature("霍格沃兹测试学院 第十期_Appium Desktop 使用_20190815 课后作业")
class TestXueQiu:
    def setup(self):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "127.0.0.1:62027",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "autoGrantPermissions": "True",
            "automationName": "Uiautomator2",
            "noReset": "true",
            "unicodeKeyboard": True,  # 使用unicode编码方式发送字符串
            "resetKeyboard": True  # 绕过软键盘
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(15)

    def teardown(self):
        self.driver.quit()

    def test_login_page(self):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/user_profile_icon").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/login_more").click()

    @allure.story("邮箱手机密码登陆，错误的手机号，断言弹框内容")
    def test_wrong_phone(self):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/user_profile_icon").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/login_more").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/login_account").send_keys("1323256526")  # 账号输入框
        self.driver.find_element(By.ID, "com.xueqiu.android:id/login_password").send_keys("123456")  # 密码输入框
        self.driver.find_element(By.ID, "com.xueqiu.android:id/button_next").click()  # 登录按钮
        text = self.driver.find_element(By.ID, "com.xueqiu.android:id/md_content").text
        assert "手机号码填写错误" in text



    @allure.story("邮箱手机密码登陆，错误的密码，断言弹框内容")
    def test_wrong_password(self):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/user_profile_icon").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/login_more").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/login_account").send_keys("13133832750")  # 账号输入框
        self.driver.find_element(By.ID, "com.xueqiu.android:id/login_password").send_keys("123456")  # 密码输入框
        self.driver.find_element(By.ID, "com.xueqiu.android:id/button_next").click()  # 登录按钮
        text = self.driver.find_element(By.ID, "com.xueqiu.android:id/md_content").text
        assert "用户名或密码错误" in text

    @pytest.mark.parametrize("search, rch", [
        ("alibaba", "阿里巴巴"),
        ("xiaomi", "小米"),
        ("google", "谷歌")
    ])
    @allure.story("数据驱动 分别搜索 alibaba xiaomi google")
    def test_search(self, search, result):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/user_profile_icon").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/login_more").click()
        self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search").click()  # 搜索输入框
        self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys(search)
        self.driver.find_element(By.ID, "com.xueqiu.android:id/name").click()
        text = self.driver.find_element(By.ID, "com.xueqiu.android:id/stockName").text
        assert result in text


if __name__ == "__main":
    pytest.main()