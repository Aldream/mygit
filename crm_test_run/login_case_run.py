'''-*- coding: utf-8-*-
@Time  : 2020/4/13
@Author: likaiquan
@File  : login_case_run.py
'''
import unittest,time
from BeautifulReport import BeautifulReport
success_testcases=unittest.defaultTestLoader.discover(\
    r'C:\Users\Shinelon\Desktop\crm_test\crm_testcase\login_case',pattern='*.py')
suite=unittest.TestSuite()
suite.addTests(success_testcases)
now=time.strftime('%Y-%m-%d-%H-%M-%S')
BeautifulReport(suite).report(filename=now+'crm登录测试报告',
                              description='crm登录测试',
                              log_path=r'C:\Users\Shinelon\Desktop\crm_test\crm_report\crm_login_report')


