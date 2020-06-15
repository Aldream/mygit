'''-*- coding: utf-8-*-
@Time  : 2020/4/13
@Author: likaiquan
@File  : login_page.py
'''
from crm_basic.crm_basic import CrmBasicClass
from selenium.webdriver.common.by import By
class LoginPage(CrmBasicClass):
    '''登录页面'''
    user_location='userNum'        #用户输入框定位
    pw_location='userPw'    #密码输入框定位
    login_location='in1'    #登录按钮定位

    def __init__(self,driver):
        self.driver=driver

    def login_input_user(self,text):
        '''用户名输入'''
        self.crm_input(By.NAME,self.user_location,text)

    def login_pwd_input(self,text):
        '''密码输入'''
        self.crm_input(By.NAME, self.pw_location, text)

    def login_click(self):
        '''登录按钮点击'''
        self.crm_click(By.ID,self.login_location)

    def login_user_attr(self,attr):
        '''获取用户名输入框属性'''
        user_attr=self.get_attribute(By.NAME,self.user_location,attr)
        return user_attr

    def login_pwd_attr(self, attr):
        '''获取密码输入框属性'''
        pw_attr=self.get_attribute(By.NAME, self.pw_location, attr)
        return pw_attr

    def login_text(self,by,value):
        '''登录页面文本获取'''
        login_text=self.get_text(by,value)
        return login_text