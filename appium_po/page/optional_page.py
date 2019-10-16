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

    # 点击切换到股票页面
    def get_stock_list(self):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/page_type_stock").click()
        return self


    def search_buttun(self):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/action_search").click()
        return self

    # 输入搜索关键字 input_text
    def search(self, keyword):
        self.driver.find_element(By.ID, "search_input_text").send_keys(keyword)
        return self

    # 关键字，联想列表
    def select(self, index):
        self.driver.find_elements(By.ID, "name")[index].click()
        return self

    def add_optional_text(self):
        self.driver.find_element(*self._optional_buttun).text
        return self

    # 长按
    def long_press(self,index):
        el = self.driver.find_elements(By.ID, "portfolio_stockName")[index]
        TouchAction(self.driver).long_press(el, duration=1000).perform()
        return self

    def click_delete_buttub(self):
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id, 'md_title') and @text = '删除']").click()
        return self

    # 点击“加自选”按钮
    def click_add_optional(self):
        self.driver.find_element(*self._follow_btn).click()
        return self

    # “已添加”按钮的状态，文本
    def followed_btn_text(self):
        return self.driver.find_element(*self._followed_btn).text

    # “加自选”按钮的状态，文本
    def follow_btn_text(self):
        return self.driver.find_element(*self._follow_btn).text
