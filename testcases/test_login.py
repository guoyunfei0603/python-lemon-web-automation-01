"""
============================
Author:小白31
Time:2020/12/20 17:19
E-mail:1359239107@qq.com
============================
"""
import pytest
from selenium.webdriver import Chrome

from common.handle_log import log
from page.login_page import LoginPage
from page.index_page import IndexPage
from casedatas.test_data import LoginData


class TestLogin():
    """登录用例"""

    # @pytest.mark.skip  # 跳过当前用例
    @pytest.mark.parametrize('item', LoginData.login_pass_data)
    def test01_login_pass(self, item, login_setup):
        """正常登录"""
        # 拆包
        login_page, index_page = login_setup

        login_page.login_pass(item["phone"], item["pwd"])

        # 断言
        res = index_page.index_info()

        try:
            assert res
        except AssertionError as e:
            log.error("用例--{}--执行失败！".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行通过！".format(item["title"]))
            # 登录成功后，点击退出登录
            login_page.logout_click()

    @pytest.mark.parametrize('item', LoginData.login_data_is_none)
    def test02_login_data_none(self, item, login_setup):
        """账号/密码数据为空"""
        login_page, index_page = login_setup
        # 访问登录页
        login_page.get_login_index()

        # 1、先走登录流程
        login_page.login_pass(item["phone"], item["pwd"])

        expected = item["expected"]

        # 2、获取错误信息提示
        res = login_page.login_get_error_info()

        # 3、断言
        try:
            assert expected == res
        except AssertionError as e:
            log.error("用例--{}--执行失败！".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行通过！".format(item["title"]))

    @pytest.mark.parametrize('item', LoginData.login_pwd_error)
    def test03_login_toast(self, item, login_setup):
        """密码错误获取toast弹窗"""
        login_page, index_page = login_setup
        # 访问登录页
        login_page.get_login_index()

        login_page.login_pass(item["phone"], item["pwd"])
        expected = item["expected"]

        # 获取toast弹窗文本
        res = login_page.login_toast_info()

        print(res)
        # 断言
        try:
            assert expected == res
        except AssertionError as e:
            log.error("用例--{}--执行失败！".format(item["title"]))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}--执行通过！".format(item["title"]))


if __name__ == '__main__':
    pytest.main(['-s'])
