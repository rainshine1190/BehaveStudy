# coding:utf-8

__author__ = 'helen'

import sys,os
from imp import reload
from behave import *

from selenium import webdriver



# 开始测试前，定义系统编码为utf-8

def before_all(context):

    reload(sys)



def before_feature(context,feature):

    context.driver = webdriver.Chrome()



def after_feature(context,feature):

    context.driver.quit()