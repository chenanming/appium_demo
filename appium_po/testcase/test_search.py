import pytests, allure
from appium_po.page.xueqiu_page import HomePage
from appium_po.base.base_driver import BaseDriver


class TestSearch01:
    def setup(self):
        self.xueqiu = HomePage()

    def test_search(self):
        assert self.xueqiu.goto_search().search("alibaba").select(0).get_price("BABA") < 170

    def test_search_text(self):
        assert "阿里" in self.xueqiu.goto_search().search("alibaba").select(-1).get_name()



if __name__ == '__main__':
    pytests.main()
