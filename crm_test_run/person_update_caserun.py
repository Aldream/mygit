'''-*- coding: utf-8-*-
@Time  : 2020/4/14
@Author: likaiquan
@File  : person_update_caserun.py
'''
import unittest,time
from BeautifulReport import BeautifulReport
testcases=unittest.defaultTestLoader.discover(\
    r'C:\Users\Shinelon\Desktop\crm_test\crm_testcase\person_info_update_case',pattern='*.py')
suite=unittest.TestSuite()
suite.addTests(testcases)
now=time.strftime('%Y-%m-%d-%H-%M-%S')
BeautifulReport(suite).report(filename=now+'crm个人资料修改测试报告',
        description='crm个人资料修改测试',
        log_path=r'C:\Users\Shinelon\Desktop\crm_test\crm_report\person_update_report')
