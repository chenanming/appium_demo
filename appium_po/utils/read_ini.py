#!/usr/bin/python3
# -*- coding=utf-8 -*-
import configparser
import pytest

class ReadInit:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = "F:/CAM/Appiumdemo/appium_po/config/LocalElement.ini"
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path, encoding='utf-8-sig')
        return read_ini

    def get_value(self, key, section=None):
        if section == None:
            section = 'login_element'
        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value
