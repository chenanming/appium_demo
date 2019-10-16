import allure
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from test_po.wework_page import Wework
from test_po.base_page import BaseDriver

class ManageToolPage(BaseDriver):
    def add_picture(self):
        self.driver.find_element(By.CSS_SELECTOR, "#menu_manageTools > span").click()  # 点击管理工具
        self.driver.find_element_by_partial_link_text("素材库").click()  # 点击素材库
        self.driver.find_element(By.CSS_SELECTOR, ".ww_icon_GrayPic").click()  # 点击图片
        element_add = self.driver.find_element(By.CSS_SELECTOR, ".js_upload_file_selector")  # 点击添加图片
        element_add.click()
        self.driver.find_element(By.CSS_SELECTOR, "#js_upload_input").send_keys(
            "F:\CAM\Appiumdemo\images\活动2.jpeg")  # 注入JS：点击上传图片，输入图片路径上传
        WebDriverWait(self.driver, 10).until( \
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".js_uploadProgress_cancel")))  # 显示等待：指定的元素不可见时，继续往下执行
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(By.CSS_SELECTOR, ".js_next"))  # 点击完成