"""
============================
Author:小白31
Time:2020/12/20 17:12
E-mail:1359239107@qq.com
============================
"""
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page.basepage import BasePage

from locator.login_loc import LoginLoc


class IndexPage(BasePage):
    """
    登录成功后的页面--前程贷首页
    """
    index_click_invest_btn_loc = (By.XPATH, '(//a[text()="抢投标"])[2]')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def index_info(self):
        """首页我的账户"""

        try:
            self.get_element_text(LoginLoc.loc_index_info, '首页_我的账户')
        except:
            return False
        else:
            return True

    def index_click_invest(self):
        """首页点击抢投标"""
        self.click_element(self.index_click_invest_btn_loc,'首页_抢投标')
