from appium_po.base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

class OptionalPage(BaseDriver):
    _search_input = (By.ID, "com.xueqiu.android:id/search_input_text")   # 首页搜索，输入
    _search_text = (By.ID, "com.xueqiu.android:id/name")                 # 搜索列表
    _md_title = ("com.xueqiu.android:id/md_titleFrame")                  # 长按页面的title
    _delete_buttun = (By.XPATH, "//*[contains(@resource-id, 'md_title') and @text = '删除']")
    _follow_btn = (By.XPATH, "//*[contains(@resource-id, 'stockCode') and @text='BABA']/../../.."
               "//*[contains(@resource-id, 'follow_btn')]")              # 加自选

    _followed_btn = (By.XPATH, "//*[contains(@resource-id, 'stockCode') and @text='BABA']/../../.."
               "//*[contains(@resource-id, 'followed_btn')]")            # 已添加

    def get_stock_list(self):
        '''点击切换到股票页面'''
        self.driver.find_element(By.ID, "com.xueqiu.android:id/page_type_stock").click()
        return self


    def search_buttun(self):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/action_search").click()
        return self

    def search(self, keyword):
        '''输入搜索关键字 input_text'''
        self.driver.find_element(By.ID, "search_input_text").send_keys(keyword)
        return self

    def select(self, index):
        '''关键字，联想列表'''
        self.driver.find_elements(By.ID, "name")[index].click()
        return self

    def long_press(self,index):
        '''选中目标，长按'''
        el = self.driver.find_elements(By.ID, "portfolio_stockName")[index]
        TouchAction(self.driver).long_press(el, duration=1000).perform()
        return self

    def click_delete_buttub(self):
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'md_title') and @text = '删除']").click()
        return self

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