# _*_ coding=utf-8 _*_
import logging
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("第十期_Selenium 第二周_20190801 课后作业")
class TestHome:
    def setup(self):
        path = "D:\ProgramData\Python36\chromedriver.exe"
        url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
        #option = webdriver.ChromeOptions()  # 代码执行前，现在cmd窗口输入chrome.exe --remote-debugging-port=8999,跳出Chrome的debuger端口
        #option.debugger_address = "127.0.0.1:8999"

        #self.driver = webdriver.Chrome(executable_path=path, options=option)
        self.driver = webdriver.Chrome(path)
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        cookies = {
            "wwrtx.d2st": "a9935414",
            "wwrtx.sid": "S-hdzeUlWX0NK7wbXNrdF1F8UDqcnLKQhTyc8mpi7pEcXzK8nFhrM9UeZJydR3Ak",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970325033079614",
            "wxpay.vid": "1688852882466545",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)
        time.sleep(20)


    @allure.story("通讯录中，添加一个成员")
    def test_loging(self):
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts > span").click()  # 点击 通讯录
        self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()  # 点击邀请成员
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".js_add_member")))
        self.driver.find_element(By.ID, "username").send_keys("test01")  # 输入姓名
        self.driver.find_element(By.NAME, "acctid").send_keys("002")  # 输入账号
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(13052652652)  # 输入手机号
        self.driver.find_element_by_link_text("保存").click()  # 点击保存按钮

    @allure.story("注入JS方法，上传文件")
    def test_upload_file(self):
        with allure.step("点击管理工具"):
            self.driver.find_element(By.CSS_SELECTOR, "#menu_manageTools > span").click()  # 点击管理工具
        print("等待。。。。。。。：" + self.driver.page_source)
        with allure.step("点击素材库"):
            self.driver.find_element_by_partial_link_text("素材库").click()  # 点击素材库
        time.sleep(5)
        with allure.step("点击图片栏"):
            self.driver.find_element(By.CSS_SELECTOR, ".ww_icon_GrayPic").click()  # 点击图片
        with allure.step("点击添加图片按钮"):
            element_add = self.driver.find_element(By.CSS_SELECTOR, ".js_upload_file_selector")  # 点击添加图片
            element_add.click()
        with allure.step("上传图片"):
            self.driver.find_element(By.CSS_SELECTOR, "#js_upload_input").send_keys(
                "F:\CAM\Appiumdemo\images\活动2.jpeg")  # 注入JS：点击上传图片，输入图片路径上传

        WebDriverWait(self.driver, 10).until( \
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".js_uploadProgress_cancel")))  # 显示等待：指定的元素不可见时，继续往下执行

        # print(self.driver.execute_script("console.log('hello from selenium')"))  # 输出
        # print(self.driver.execute_script("return document.title;"))  # 打印
        with allure.step("点击完成"):
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(By.CSS_SELECTOR, ".js_next"))  # 点击完成


    def teardown(self):
        self.driver.quit()

if __name__ == "__main__":
    pytest.main()