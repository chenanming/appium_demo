from test_po.base_page import BaseDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BaseDriver):
    _edit = (By.CSS_SELECTOR, ".js_edit")          # 编辑
    _disable = (By.CSS_SELECTOR, ".js_disable")    # 禁用
    _delete = (By.CSS_SELECTOR, ".js_del_member")  # 删除
    _invite = (By.CSS_SELECTOR, ".js_move_top")    # 置顶/取消置顶
    _username = (By.ID, "username")                # 姓名
    _save =(By.CSS_SELECTOR, ".js_save")           # 保存
    _tips = (By.CSS_SELECTOR, ".success")          # 提示

    def update(self, **kwargs):
        '''编辑用户'''
        self.click_by_js(*self._edit)                           # 点击 编辑
        element = self.driver.find_element(*self._username)     #
        element.clear()                                         # 清除用户名字
        element.send_keys(kwargs["name"])                       # 填写新的用户名字
        self.driver.find_element(*self._save).click()           # 点击 保存
        tips = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*self._tips))
        assert tips.text == "保存成功"
        return self

    def disable(self):
        '''禁用用户'''
        self.click_by_js(*self._disable)
        pass

    def delete(self):
        '''删除用户'''
        self.click_by_js(*self._delete)
        pass

    def invite(self):
        '''置顶或取消用户'''
        self.click_by_js(*self._invite)
        pass