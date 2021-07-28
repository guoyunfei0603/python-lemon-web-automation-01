"""
============================
Author:小白31
Time:2020/12/24 21:34
E-mail:1359239107@qq.com
============================
"""
import pytest
from selenium.webdriver import Chrome

from common.handle_config import conf
from page.index_page import IndexPage
from page.invest_page import InvestPage
from page.login_page import LoginPage
from page.user_page import UserPage
from selenium import webdriver

def create_driver():
    """
    打开浏览器，创建driver对象
    :return:
    """
    if conf.getboolean('run','headless'):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
    return driver


@pytest.fixture(scope='class')
def login_setup():

    driver = create_driver()
    driver.implicitly_wait(10)
    driver.get(conf.get('env', 'base_url') + conf.get('url_path', 'login'))
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page, index_page


@pytest.fixture(scope='class')
def invest_fixtrue():
    driver = create_driver()
    driver.maximize_window()
    driver.implicitly_wait(15)

    login_page = LoginPage(driver)
    # 打开登录页面
    login_page.get_login_index()
    # 登录
    login_page.login_pass(conf.get('test_data', 'phone'), conf.get('test_data', 'pwd'))
    # 投资页面
    invest_page = InvestPage(driver)
    # 用户页面
    user_page = UserPage(driver)

    # 点击抢投标
    index_page = IndexPage(driver)
    index_page.index_click_invest()

    yield invest_page, user_page
    driver.quit()