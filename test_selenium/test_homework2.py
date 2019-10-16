# _*_ coding=utf-8 _*_
''' 以testerhome网站作为待测对象

最新发布的帖子浏览
社区访问霍格沃兹测试学院，断言未登录是被拒绝的
错误用户名和密码登陆
搜索”测试媛“，找到成立的那个帖子，进去后断言标题与搜索出来的标题是对应的
把代码和allure的截图，贴到回复里

allure测试报告
pytest test_demo.py --alluredir report/demo       #生成xml报告用这个命令
allure generate report/demo/ -o report/demo/html  # 生成html格式报告
'''
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@allure.feature("课后作业")
class TestSelenium:
    def setup_method(self):
        path = "D:\ProgramData\Python36\chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(20)

    @allure.story("最新发布的帖子浏览")
    def test_newtopics(self):
        self.driver.find_element_by_link_text("社区").click()
        self.driver.find_element_by_link_text("最新发布").click()

    @allure.story("社区访问霍格沃兹测试学院，断言未登录是被拒绝的")
    def test_login(self):
        self.driver.find_element_by_css_selector("a[href*='/teams']").click()
        self.driver.find_element_by_css_selector('a[data-name*="霍格沃兹测试学院"]').click()
        self.driver.find_element_by_css_selector('a[title*="第十期_selenium 进阶_20190728"]').click()
        time.sleep(10)
        assert "访问被拒绝，你可能没有权限或未登录。" in self.driver.page_source

    @allure.story("错误用户名和密码登陆")
    @pytest.mark.parametrize("username, password", [
        ("tester", "123456"),
        ("1313383249@163.com", "123456")
    ])
    def test_Abnormal_login(self, username, password):
        self.driver.find_element_by_xpath('//*[contains(text(), "登录")]').click()
        self.driver.find_element_by_xpath('//*[@id="user_login"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(password)
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(10)
        assert "帐号或密码错误。" \
               or "由于多次密码错误，您的帐号已被暂时锁定，一小时后将自动解锁，或者你可以通过邮件手动解锁" \
               in self.driver.page_source

    @allure.story("搜索”测试媛“，找到成立的那个帖子，进去后断言标题与搜索出来的标题是对应的")
    def test_search(self):
        self.driver.find_element_by_xpath('//input[@name="q"]').send_keys("测试媛")
        self.driver.find_element_by_xpath('//input[@name="q"]').send_keys(Keys.ENTER)  # 搜索“测试媛”，然后回车
        self.driver.find_element_by_xpath('//*[@class="panel-body"]/div[4]/div/a').click()
        time.sleep(10)
        assert "与 Bug 战斗的测试媛女神们，撑起了互联网软件质量半边天" in self.driver.page_source

    def teardown_method(self):
        self.driver.quit()

if __name__ == "__main__":
    pytest.main()