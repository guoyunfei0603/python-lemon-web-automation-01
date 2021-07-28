"""
============================
Author:小白31
Time:2021/1/10 17:39
E-mail:1359239107@qq.com
============================
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from page.basepage import BasePage


class UserPage(BasePage):
    """用户页面"""

    user_invest_amount_loc = (By.XPATH,'//li[@class="color_sub"]')

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def get_user_invest_amount(self):
        """获取用户投资余额"""

        text = self.get_element_text(self.user_invest_amount_loc)
        user_amount = text[:-1]
        return user_amount
