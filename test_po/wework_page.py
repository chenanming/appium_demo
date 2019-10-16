
from selenium import webdriver

class Wework:
    def __init__(self):
        path = "D:\ProgramData\Python36\chromedriver.exe"
        url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
        # option = webdriver.ChromeOptions()  # 代码执行前，现在cmd窗口输入chrome.exe --remote-debugging-port=8999,跳出Chrome的debuger端口
        # option.debugger_address = "127.0.0.1:8999"

        # self.driver = webdriver.Chrome(executable_path=path, options=option)
        self.driver = webdriver.Chrome(path)
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        cookies = {
            "wwrtx.d2st": "a2557794",
            "wwrtx.sid": "S-hdzeUlWX0NK7wbXNrdF1nwqmOxpUBQSzlTq4mqhJ-40y5OrOEseE_yubrRFSqH",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970325033079614",
            "wxpay.vid": "1688852882466545",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)