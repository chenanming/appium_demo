# -*- coding=utf-8 -*-
from utils.read_ini import ReadInit
from appium_po.base.base_driver import BaseDriver

class GetByLocal(BaseDriver):

    def get_element(self, key):
        read_ini = ReadInit()
        local = read_ini.get_value(key)
        if local != None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                elif by =='android':
                    return self.driver.find_element_by_android_uiautomator(local_by)
                else:
                    return self.driver.find_element_by_xpath(local_by)
            except:
                return None
        else:
            return None