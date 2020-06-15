'''-*- coding: utf-8-*-
@Time  : 2020/4/13
@Author: likaiquan
@File  : login_fail_case.py
'''
import unittest,time
from ddt import ddt,data,unpack,file_data
from selenium import webdriver
from crm_process.login_process import LoginProcess

class LoginFailCase(unittest.TestCase):

    def setUp(self) -> None:
        driver=webdriver.Chrome()
        self.login_driver=LoginProcess(driver)
        print('测试开始')

    # @data(*d)
    # @unpack
    @file_data(r'C:\Users\Shinelon\Desktop\crm_test\crm_data\crm_login_data\user.json')
    def test_01(self, username, password, hope_alert):
        self.login_driver.login(username, password)
        self.assertEqual(self.login_driver.alert_text().strip(), hope_alert, msg='与预期提示不符')

    def tearDown(self) -> None:
        time.sleep(1)
        self.login_driver.crm_quit()
        print('测试结束')