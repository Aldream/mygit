'''-*- coding: utf-8-*-
@Time  : 2020/4/13
@Author: likaiquan
@File  : crm_basic.py
'''
from selenium import webdriver
from selenium.webdriver.support.select import Select

class CrmBasicClass():
    '''crm基础类，存放需要用到的元素定位、点击、输入等操作'''
    crm_url='http://localhost:8080/crm/'

    def __init__(self,driver):
        self.driver=driver
        # self.driver=webdriver.Chrome()

    def open_crm(self,url,title):
        '''打开页面'''
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        try:
            assert self.driver.title==title,'实际标题与预期标题不符'
        except Exception as e:
            print(e)

    def findElement(self,by,value):
        '''元素定位'''
        try:
            element=self.driver.find_element(by,value)
        except Exception as e:
            print('页面未找到该元素',e)
        return element

    def crm_click(self,by,value):
        '''点击操作'''
        self.findElement(by,value).click()

    def crm_input(self,by,value,text):
        '''输入操作'''
        self.findElement(by,value).send_keys(text)

    def text_clear(self,by,vlaue):
        '''文本清除操作'''
        self.findElement(by,vlaue).clear()

    def get_text(self,by,value):
        '''获取文本信息'''
        text=self.findElement(by,value).text
        return text

    def get_attribute(self,by,value,att_name):
        '''获取属性信息'''
        attr_value=self.findElement(by,value).get_attribute(att_name)
        return attr_value

    def crm_screenshot(self,file_name):
        self.driver.get_screenshot_as_file(file_name)

    def switch_frame(self,by,value):
        '''切换到frame'''
        self.driver.switch_to.default_content()
        frame=self.findElement(by,value)
        self.driver.switch_to.frame(frame)

    def crm_select_ele(self,by,value):
        '''通过元素定位选值'''
        self.findElement(by,value)

    def crm_select(self,by,location):
        '''下拉框定位'''
        return Select(self.findElement(by,location))

    def crm_select_by_value(self,by,location,value):
        '''通过下拉框的value选值'''
        select=self.crm_select(by,location)
        select.select_by_value(value)

    def crm_select_by_text(self,by,location,text):
        '''通过下拉框的文本定位'''
        select=Select(self.findElement(by,location))#定位到下拉框
        select.select_by_visible_text(text)

    def switch_alert(self):
        '''切换到弹出框'''
        alert1=self.driver.switch_to.alert
        return alert1

    def alert_text(self):
        '''获取弹出框文本'''
        alert_text=self.switch_alert().text
        return alert_text

    def alert_accept(self):
        '''弹出框点击确定'''
        self.switch_alert().accept()

    def alert_dismiss(self):
        '''弹出框点击取消'''
        self.switch_alert().dismiss()

    def crm_quit(self):
        '''关闭操作'''
        self.driver.quit()

