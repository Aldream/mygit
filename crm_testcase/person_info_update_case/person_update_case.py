'''-*- coding: utf-8-*-
@Time  : 2020/4/14
@Author: likaiquan
@File  : person_update_case.py
'''
import unittest
from ddt import ddt,data
from selenium import webdriver
from crm_page.person_info_update import PersonInfoUpdate
from crm_process.login_process import LoginProcess
d=['初中','高中','本科','博士','硕士']
@ddt
class PersonUpdateCase(unittest.TestCase):
    def setUp(self) -> None:
        driver=webdriver.Chrome()
        self.up_driver=PersonInfoUpdate(driver)
        self.login_driver=LoginProcess(driver)
        self.login_driver.login('admin','123456')
        self.up_driver.click_person_info()
        self.up_driver.switch_mainframe()
    def test_01(self):
        '''性别选择女'''

        self.up_driver.select_female()
        self.up_driver.click_submit()
        alert_text=self.up_driver.alert_text()
        self.up_driver.alert_accept()
        self.assertEqual(alert_text.strip(),'员工修改成功',msg='提示与预期不符')

    def test_02(self):
        '''性别选择男'''

        self.up_driver.select_male()
        self.up_driver.click_submit()
        alert_text = self.up_driver.alert_text()
        self.up_driver.alert_accept()
        self.assertEqual(alert_text.strip(), '员工修改成功', msg='提示与预期不符')

    @data(d)
    def test_03(self,value):
        self.up_driver.select_depart(value)
        self.up_driver.click_submit()
        alert_text = self.up_driver.alert_text()
        self.assertEqual(alert_text.strip(), '员工修改成功', msg='提示与预期不符')
    def tearDown(self) -> None:
        self.up_driver.crm_quit()
        print('测试结束')