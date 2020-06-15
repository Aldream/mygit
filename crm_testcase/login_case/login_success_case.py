'''-*- coding: utf-8-*-
@Time  : 2020/4/13
@Author: likaiquan
@File  : login_success_case.py
'''
import unittest,time
from selenium import webdriver
from crm_process.login_process import LoginProcess
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack
fp=open(r'C:\Users\Shinelon\Desktop\crm_test\crm_data\crm_login_data\login_success_data.txt',
          'r',encoding='utf-8-sig')
d=[]
for line in fp.readlines():
    line=line.strip().split(',')
    d.append(line)
fp.close()
@ddt
class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:
        driver=webdriver.Chrome()
        self.login_driver=LoginProcess(driver)
        print('测试开始')

    @data(*d)
    @unpack
    def test_01(self,username,password,hope_text):
        '''输入正确的用户名密码登录成功，用户信息显示正确'''
        self.login_driver.login(username,password)
        self.login_driver.switch_frame(By.ID,'topFrame')
        text=self.login_driver.get_text(By.XPATH,\
        '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div')
        self.assertEqual(text.strip(),hope_text,msg='与预期不符')

    def tearDown(self) -> None:
        time.sleep(2)
        self.login_driver.crm_quit()
        print('测试结束')