# _*_ coding=utf-8 _*_
import logging
import time

import pytests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHome:
    def setup(self):
        option = webdriver.ChromeOptions() # 开启chrome的debug接口，端口是8999
        option.debugger_address = '127.0.0.1:8999'

        self.driver = webdriver.Chrome(chrome_options=option) # selenium驱动链接Chrome的debug调试端口，实现自动化
        self.driver.get("https://testerhome.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_1(self):
        self.driver.find_element_by_partial_link_text("先到先得").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".title [href*='/topics/19682']").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".title [title*='先到先得']").click()
        self.driver.find_element_by_link_text("https://testerhome.com/topics/19664").click()
        handles = self.driver.window_handles  # 先获得所有句柄，再循环遍历是否是当前窗口
        for handle in handles:
            if self.driver.current_window_handle != handle:
                self.driver.switch_to_window(handle)
        value = self.driver.find_element_by_id("有奖投票").text
        assert value == "有奖投票"

        #ActionChains(self.driver).\
        #   click_and_hold(self.driver.find_element_by_css_selector(".reply-buttons .total"))\
        #    .move_by_offset(30, 50).release().perform()

        #self.driver.execute_script("window.scrollto(0, 500)") # 滚动屏幕
        #self.driver.find_element(By.CSS_SELECTOR, ".form-header__title").click()

        logging.info(self.driver.page_source)
        #logging.info(len(self.driver.find_element_by_xpath("//*[@class='ant-checkbox-input']")))
        self.driver.find_element(By.CSS_SELECTOR, ".ant-checkbox-input").click()

    def test_expected_brower(self):
        self.driver.find_element_by_partial_link_text("社区").click()
        self.driver.find_element_by_partial_link_text("最新发布").click()
        #self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/div[1]/div/a').click()
        #self.driver.find_element(By.XPATH, '//*[@id="main-page"]/div[2]/div/ul/li[6]/a').click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".topic .title a")))

    def teardown(self):
        pass
        #self.driver.quit()

if __name__ == "__main__":
    pytests.main()