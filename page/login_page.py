"""
============================
Author:小白31
Time:2020/12/20 15:42
E-mail:1359239107@qq.com
============================
"""
from selenium.webdriver.chrome.webdriver import WebDriver

from common.handle_config import conf
from locator.login_loc import LoginLoc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.basepage import BasePage


class LoginPage(BasePage):
    """
    登录页面封装动作
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_pass(self, phone, pwd):
        """正常登录"""

        # 输入账号
        # mobile_input = self.driver.find_element(*LoginLoc.loc_phone)
        # mobile_input.clear()
        # mobile_input.send_keys(phone)
        self.input_send_keys(loc=LoginLoc.loc_phone,value=phone,loc_desc='登录页面_输入手机号')
        # 输入密码
        # pwd_input = self.driver.find_element(*LoginLoc.loc_pwd)
        # pwd_input.clear()
        # pwd_input.send_keys(pwd)

        self.input_send_keys(loc=LoginLoc.loc_pwd,value=pwd,loc_desc='登录页面_输入密码')

        # 点击登录
        self.click_element(LoginLoc.loc_login_button,'登录页面_登录按钮')

    def login_get_error_info(self):
        """登录账号/密码为空获取错误提示"""
        self.wait_visibility_ele(LoginLoc.loc_error_info,'登录页面_为空获取提示')
        return self.get_element_text(LoginLoc.loc_error_info,'登录页面_为空获取提示')

    def login_toast_info(self):
        """登录获取toast弹窗提示"""
        toast_info = LoginLoc.loc_toast_info

        self.wait_visibility_ele(LoginLoc.loc_toast_info,'登录页面_获取toast弹窗提示')
        return self.get_element_text(LoginLoc.loc_toast_info,'登录页面_获取toast弹窗提示')


    def logout_click(self):
        """退出登录"""
        self.click_element(LoginLoc.loc_logout_button)

    def get_login_index(self):
        """访问登录页"""
        self.driver.get(conf.get('env', 'base_url') + conf.get('url_path', 'login'))