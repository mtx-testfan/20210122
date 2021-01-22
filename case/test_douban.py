#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---

# ss1:先完成一个登陆案例
import os
import random
import time

import pytest
from appium import webdriver
from time import sleep

from data.ReadData import elements_data
from page.base_driver import BaseDriver

# 1.先抽离启动项 和 driver
# 2.pytest改造
from page.homePage import homepage
from page.loginDouban import LoginPage

'''

调试case层
'''
# class Test_login():
#     def setup_class(self):
#         self.driver = BaseDriver.start_driver\
#             (appPackage='com.douban.frodo',appActivity='com.douban.frodo.activity.SplashActivity')
#
#     def test_login_case(self):
#         # 1.读取元素定位表达式
#         page_obj = homepage(self.driver)
#         page_obj.login()
#
#     def teardown_class(self):
#         self.driver.quit()


class TestDouBanLogin():

    def test_case_01(self, driver):
        login = LoginPage(driver)
        # 调用登录这个业务
        login.login_pass('17610873228','yaoyao123456')
        time.sleep(10)
        # 准备开始断言
        login.click_me()
        time.sleep(3)
        assert '嘟嘟' in login.get_page_source


if __name__ == '__main__':
    pytest.main(['-sv'])