'''-*- coding: utf-8-*-
@Time  : 2020/4/14
@Author: likaiquan
@File  : person_info_update_process.py
'''
from crm_page.person_info_update import PersonInfoUpdate
class PersonUpdateProcess(PersonInfoUpdate):
    def __init__(self,driver):
        PersonInfoUpdate.__init__(self,driver)
    def update_deplma(self,text):
        self.select_depart(text)
