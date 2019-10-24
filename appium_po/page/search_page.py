from time import sleep
from appium_po.base.base_driver import BaseDriver
from selenium.webdriver.common.by import By


class SearchPage(BaseDriver):
    _search_input = (By.ID, "com.xueqiu.android:id/search_input_text")     # 首页搜索，输入
    _search_text = (By.ID, "com.xueqiu.android:id/name")                   # 搜索列表
    _follow_btn = (By.XPATH, "//*[contains(@resource-id, 'stockCode') and @text='BABA']/../../.."
                             "//*[contains(@resource-id, 'follow_btn')]")  # 加自选
    _followed_btn = (By.XPATH, "//*[contains(@resource-id, 'stockCode') and @text='BABA']/../../.."
                               "//*[contains(@resource-id, 'followed_btn')]")  # 已添加


    def search(self, keyword):
        # 输入搜索关键字 input_text
        self.driver.find_element(By.ID, self.element.get_value('搜索输入')).send_keys(keyword)  # 用ReadIni()方法读取元素
        #self.driver.find_element(By.ID, "search_input_text").send_keys(keyword)
        return self

    def select(self, index):
        # 关键字，联想列表
        self.driver.find_elements(By.ID, "name")[index].click()
        return self

    def get_price(self, stock_type):
        '''获取'''
        price = float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'stockCode') and @text='"
            + stock_type
            + "']/../../.."
              "//*[contains(@resource-id, 'current_price')]").text)
        return price


    def click_add_optional(self):
        '''点击【加自选】按钮'''
        self.driver.find_element(*self._follow_btn).click()
        return self

    def followed_btn_text(self):
        '''【已添加】按钮的状态，文本'''
        return self.driver.find_element(*self._followed_btn).text

    def follow_btn_text(self):
        '''【加自选】按钮的状态，文本'''
        return self.driver.find_element(*self._follow_btn).text