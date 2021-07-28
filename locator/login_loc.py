"""
============================
Author:小白31
Time:2020/12/20 15:37
E-mail:1359239107@qq.com
============================
"""
from selenium.webdriver.common.by import By


class LoginLoc():
    """
    登录相关的定位元素表达式
    """
    # 定位账号
    loc_phone = (By.XPATH, '//input[@placeholder="手机号"]')
    # 定位密码
    loc_pwd = (By.XPATH, '//input[@placeholder="密码"]')
    # 点击登录
    loc_login_button = (By.XPATH, '//button[text()="登录"]')
    # 定位错误信息提示
    loc_error_info = (By.XPATH, '//div[@class="form-error-info"]')
    # 定位toast弹窗
    loc_toast_info = (By.XPATH, '//div[@class="layui-layer-content"]')
    # 首页--我的账户
    loc_index_info = (By.XPATH,"//a[contains(text(),'我的帐户')]")
    # 首页--退出按钮
    loc_logout_button = (By.XPATH,'//a[text()="退出"]')