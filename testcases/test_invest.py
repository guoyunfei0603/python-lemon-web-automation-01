import pytest
import time
from casedatas.test_data import InvestData




class TestInvest():
    @pytest.mark.parametrize('item',InvestData.error_data)
    def test_invest_btn_info(self, item,invest_fixtrue):
        """投资按钮错误提示"""
        invest_page, user_page = invest_fixtrue

        # 输入投资金额
        invest_page.input_invest_amount(item['money'])
        # 获取投标按钮提示
        res = invest_page.get_invest_btn_info()
        expected = item['expected']
        # 断言
        assert res == expected
        time.sleep(3)

    @pytest.mark.parametrize('item',InvestData.error_popup_data)
    def test_window_err_info(self, item,invest_fixtrue):
        """弹窗错误提示"""
        invest_page, user_page = invest_fixtrue

        # 1. 输入投资金额
        invest_page.input_invest_amount(item['money'])
        # 2.点击投标
        invest_page.click_invest_btn()
        time.sleep(3)
        # 3. 获取弹窗的错误提示
        res = invest_page.get_window_err_info()

        invest_page.close_err_window()

        expected = item['expected']
        # 4. 断言
        assert res == expected


    @pytest.mark.parametrize('item',InvestData.success_data)
    def test_window_success_info(self,item, invest_fixtrue):
        invest_page, user_page = invest_fixtrue
        invest_page.window_scrollto()

        # 先获取投资输入框里面的余额
        start_amount = invest_page.get_invest_input_amount()

        # 1. 输入投资金额
        invest_page.input_invest_amount(item['money'])
        # 2. 点击投标
        invest_page.click_invest_btn()
        time.sleep(1)
        # 3. 获取弹窗提示
        res = invest_page.get_success_window_info()
        expected = item['expected']
        # 3. 断言
        assert res == expected
        time.sleep(3)
        # 4. 点击查看并激活
        invest_page.click_check_activate()
        # 5. 跳转到用户页面，获取余额

        end_amount = user_page.get_user_invest_amount()
        assert float(start_amount) - float(end_amount) == item['money']


