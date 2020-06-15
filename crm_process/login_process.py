'''-*- coding: utf-8-*-
@Time  : 2020/4/13
@Author: likaiquan
@File  : login_process.py
'''
from selenium import webdriver
from crm_page.login_page import LoginPage
class LoginProcess(LoginPage):
    def __init__(self,driver):
        self.driver=driver
    def login(self,username,password):
        '''登录流程'''
        self.open_crm(self.crm_url,'CRM客户关系管理系统_用户登录')
        self.login_input_user(username)
        self.login_pwd_input(password)
        self.login_click()