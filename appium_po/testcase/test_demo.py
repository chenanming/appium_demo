#!/usr/bin/python3
# -*- coding=utf-8 -*-
import pytest
from time import sleep
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium_po.page.optional_page import OptionalPage
from appium_po.page.search_page import SearchPage
from selenium.webdriver.common.by import By

capabilities = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "127.0.0.1:62027",
    "appPackage": "com.tencent.mm",
    "appActivity": ".ui.LauncherUI",
    "autoGrantPermissions": True,
    "automationName": "Appium",
    #"noReset": True,
    "chromeOptions": {'androidProcess': 'com.tencent.mm:appbrand0'}
    #"unicodeKeyboard": True,  # 使用unicode编码方式发送字符串
    #"resetKeyboard": True  # 绕过软键盘
}

class HomePage:
    def __init__(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(15)


    def get_toast(self, message):
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % message)
            WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(toast_loc))
            return True
        except:
            return False

    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5    # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def test(self):
        '''点开小程序'''
        self.driver.find_elements_by_id("com.tencent.mm:id/r9")[0].click()
        time.sleep(4)
        print(self.driver.contexts)

        # 注意，这里是不需要切换的，别踩坑了！！！！！！
        # driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        time.sleep(3)

        # tap触摸右下角那个菜单坐标 [873,1654], [1080,1861]
        self.driver.tap([(873, 1654), (1080, 1861)], 500)

        # 点发红包赚赏金
        self.driver.find_element_by_accessibility_id("发红包赚赏金").click()

    def get_sms(self):
        self.driver.send_sms("15267079102", "welecome here")

if __name__ == '__main__':
    driver = HomePage()
    driver.swipeDown()
    driver.test()