import pytest, allure
from appium_po.page.xueqiu_page import HomePage

print()
'''
课后作业
点击自选，添加股票，判断股票添加成功
再次添加股票，添加股票的按钮要变成“已添加”
删除已经添加的股票，再次搜索股票，股票的按钮变成“加自选”
注意“自选”菜单，可能会动态浮动
'''

@allure.feature("第十期_Appium 使用进阶_20190818 课后作业")
class TestSearch:
    def setup(self):
        self.xueqiu = HomePage()

    def teardown(self):
        self.xueqiu.driver.quit()

    @allure.story("添加股票，判断股票添加成功")
    def test_search_add_optional(self):
        self.xueqiu.goto_search().search("alibaba").select(0).click_add_optional()

        print(self.xueqiu.get_toast("添加成功"))
        assert self.xueqiu.get_toast('添加成功') == True


    @allure.story("再次添加股票，添加股票的按钮要变成“已添加”")
    def test_add_optional_agine(self):
        assert self.xueqiu.goto_search().search("alibaba").select(0).followed_btn_text() == "已添加"

    @allure.story("删除已经添加的股票，再次搜索股票，股票的按钮变成“加自选”")
    def test_deletat_optional(self):
        self.xueqiu.goto_optional().long_press(0).click_delete_buttub()
        assert self.xueqiu.get_toast('已从自选删除') == True
        assert self.xueqiu.goto_optional().search_buttun().search("alibaba").select(0).follow_btn_text() == "加自选"

if __name__ == '__main__':
    pytest.main()