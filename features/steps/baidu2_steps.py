import time
from behave import *

# @given(u'open the browser')
# def step_given(context):
#     print('打开浏览器')
#     context.driver.get('http://www.baidu.com')
#     print(context.driver)
#
#
# @when(u'input and search')
# def step_when(context):
#     print('输入并搜索')
#     context.baidu_page().InputAndSearch()
#
#     time.sleep(5)
#
#
#
# @then(u'close the browser')
# def step_then(context):
#     print('断言并，关闭浏览器')
#     assert 1 == 1

@step('open the browser')
def step_impl(context):
    context.baidu_page.GetUrl('http://www.baidu.com')


@step('input and search')
def step_impl(context):
    context.baidu_page.InputAndSearch()


@step('close the browser')
def step_impl(context):
    context.baidu_page.ClosePage()