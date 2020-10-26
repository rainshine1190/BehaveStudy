from features.pages.baidu_page import baidu_page

def feature_initialize(context,driver):
    context.baidu_page = baidu_page(driver)