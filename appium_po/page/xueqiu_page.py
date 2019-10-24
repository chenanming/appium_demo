#!/usr/bin/python3
# -*- coding=utf-8 -*-
import logging

import pytest
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium_po.page.optional_page import OptionalPage
from appium_po.page.search_page import SearchPage
from selenium.webdriver.common.by import By


class HomePage:
    _search_but=(By.ID, "com.xueqiu.android:id/home_search")  # 首页搜索框

    def __init__(self):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "127.0.0.1:62027",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "autoGrantPermissions": True,
            "automationName": "Uiautomator2",
            "noReset": True,
            "unicodeKeyboard": True,  # 使用unicode编码方式发送字符串
            "resetKeyboard": True  # 绕过软键盘
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(15)

    def get_toast(self, message):
        '''验证弹窗提示'''
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % message)
            WebDriverWait(self.driver, 100, 0.5).until(EC.presence_of_element_located(toast_loc))
            return True
        except:
            return False

    def get_attribute(self):
        print(self.driver.find_element_by_id("user_profile_home").get_attribute("class"))

    def get_page_source(self):
        '''获取页面信息'''
        try:
            text = self.driver.page_source
            logging.info("get page source success")
            return text
        except:
            logging.info("get page source is 'fail'")

    def swipeLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipeRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.35
        y2 = l['height'] * 0.65
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.65
        y2 = l['height'] * 0.35
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def goto_search(self):
        '''点击搜索，进入搜索页面'''
        self.driver.find_element(*self._search_but).click()
        return SearchPage(self.driver)

    def goto_optional(self):
        '''自选页'''
        self.driver.find_element_by_android_uiautomator('className("android.widget.TextView").text("自选")').click()
        return OptionalPage(self.driver)


if __name__ == '__main__':
    pytest.main()