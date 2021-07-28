from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page.basepage import BasePage


class InvestPage(BasePage):
    """投资页面封装方法"""

    input_invest_amount_loc = (By.XPATH, '//input[@data-url="/Invest/invest"]')
    invest_btn_loc = (By.XPATH, '//button[@class="btn btn-special height_style"]')
    window_err_info_loc = (By.XPATH, '//div[@class="text-center"]')
    close_err_window_loc = (By.XPATH, '//a[text()="确认"]')
    success_window_info_loc = (By.XPATH, '(//div[@class="capital_font1 note"])[2]')
    click_check_activate_loc = (By.XPATH, '(//button[text()="查看并激活"])[2]')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def input_invest_amount(self, amount):
        """输入投资金额"""
        self.input_send_keys(self.input_invest_amount_loc,amount, '投资页面_输入投资金额')

    def click_invest_btn(self):
        """点击投标按钮"""
        self.click_element(self.invest_btn_loc, '投资页面_点击投标按钮')

    def get_invest_btn_info(self):
        """获取投标按钮的提示"""
        return self.get_element_text(self.invest_btn_loc,'投资页面_投标按钮提示')


    def get_window_err_info(self):
        """获取弹窗错误提示"""
        self.wait_visibility_ele(self.window_err_info_loc,'投资页面_错误弹窗提示')
        return self.get_element_text(self.window_err_info_loc,'投资页面_错误弹窗提示')


    def close_err_window(self):
        """关闭错误弹窗提示"""
        self.click_element(self.close_err_window_loc,'投资页面_关闭错误弹窗提示')

    def get_success_window_info(self):
        """获取投资成功的弹窗提示"""
        self.wait_visibility_ele(self.success_window_info_loc,'投资页面_投资成功弹窗提示')
        return self.get_element_text(self.success_window_info_loc,'投资页面_投资成功弹窗提示')

    def get_invest_input_amount(self):
        """获取投资输入框中的余额"""
        return self.get_element_attr(self.input_invest_amount_loc,'data-amount','投资页面_获取投资输入框的余额')

    def click_check_activate(self):
        """点击查看并激活"""
        self.click_element(self.click_check_activate_loc,'投资页面_点击查看并激活')

    def window_scrollto(self):
        """窗口滑动300"""
        js = """
        window.scrollTo(0,300)
        """
        self.driver.execute_script(js)
