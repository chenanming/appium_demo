# _*_ coding=utf-8 _*_

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHome:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(10)

    def test_1(self):
        #self.driver.find_element_by_partial_link_text("如何做好性能压测").click()
        self.driver.find_element(By.CSS_SELECTOR, ".title [title*='如何做好性能压测']").click()
        self.driver.find_element_by_class_name("btn-default").click()  # 点击目录
        self.driver.find_element_by_link_text("100工人的问题").click()  # 点击子目录
        self.driver.find_element(By.CSS_SELECTOR)

    def teardown_method(self):
        self.driver.quit()

if __name__ == "__main__":
    pytest.main()