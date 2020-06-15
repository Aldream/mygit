'''-*- coding: utf-8-*-
@Time  : 2020/4/13
@Author: likaiquan
@File  : person_info_update.py
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from crm_basic.crm_basic import CrmBasicClass
from crm_process.login_process import LoginProcess
class PersonInfoUpdate(LoginProcess,CrmBasicClass):
    person_info_location='/html/body/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[4]/div/a'
    female_location='//input[@name="userSex" and @value="女"]'
    male_location='//input[@name="userSex" and @value="男"]'
    diploma_select_location='userDiploma'
    depart_select_location='departmentId'
    tel_location='/html/body/form/table[1]/tbody/tr[6]/td[2]/input'
    salary_location='/html/body/form/table[1]/tbody/tr[7]/td[2]/input'
    id_location='/html/body/form/table[1]/tbody/tr[8]/td[2]/input'
    e_mail_location='/html/body/form/table[1]/tbody/tr[10]/td[2]/input'
    submit_location='/html/body/form/table[2]/tbody/tr/td[2]/input'
    back_location='/html/body/form/table[2]/tbody/tr/td[3]/input'
    def __init__(self,driver):
        CrmBasicClass.__init__(self,driver)

    def __input_update(self,value,text):
        '''输入框文本修改'''
        self.text_clear(By.XPATH,value)
        self.crm_input(By.XPATH,value,text)

    def __select_update(self,value,text):
        '''个人信息修改界面下拉框文本进行选择'''
        self.crm_select_by_text(By.NAME,value,text)

    def switch_topframe(self):
        '''切换至topFrame'''

        self.switch_frame(By.NAME,'topFrame')

    def switch_mainframe(self):
        '''切换至mainFrame'''
        self.switch_frame(By.NAME,'mainFrame')

    def click_person_info(self):
        '''点击修改个人信息'''
        self.switch_topframe()
        time.sleep(2)
        self.crm_click(By.XPATH,self.person_info_location)

    def select_sex(self,text):
        self.crm_click(By.XPATH,)
    def select_female(self):
        '''选择性别女'''
        self.crm_click(By.XPATH,self.female_location)

    def select_male(self):
        '''选择性别男'''
        self.crm_click(By.XPATH,self.male_location)

    def get_female_attr(self,attri):
        '''获取性别女属性'''
        self.get_attribute(By.NAME,self.female_location,attri)

    def get_male_attr(self,attri):
        '''获取性别男属性'''
        self.get_attribute(By.NAME,self.male_location,attri)

    def select_diploma_value(self,text):
        '''选择文凭'''
        self.__select_update(self.diploma_select_location,text)

    def select_depart(self,text):
        '''部门选择'''
        self.__select_update(self.depart_select_location,text)

    def tel_update(self,text):
        '''修改座机号码'''
        self.__input_update(self.tel_location,text)

    def salary_update(self,text):
        '''修改座机号码'''
        self.__input_update(self.salary_location,text)

    def id_update(self,text):
        '''修改身份证号'''
        self.__input_update(self.id_location,text)

    def e_mail_update(self,text):
        self.__input_update(self.e_mail_location,text)

    def click_submit(self):
        '''点击提交'''
        self.crm_click(By.XPATH,self.submit_location)

    def click_quit(self):
        '''点击返回'''
        self.crm_click(By.XPATH,self.back_location)


if __name__=="__main__":
    driver=webdriver.Chrome()
    test_driver=PersonInfoUpdate(driver)
    test_driver.login('admin','123456')
    test_driver.click_person_info()
    test_driver.switch_mainframe()
    test_driver.select_female()
    time.sleep(2)
    test_driver.click_submit()




