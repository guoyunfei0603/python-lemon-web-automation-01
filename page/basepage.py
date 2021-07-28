
import os
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.handle_log import log
from common.handle_path import ERROR_IMAGE


class BasePage:
    """基础的页面类，封装一些页面中通用的操作方法"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_visibility_ele(self, loc, loc_desc='', timeout=20, poll_time=0.5):
        """
        等待元素可见
        :param loc: loc: 元素的定位器 -->:(BY.xxx,'表达式')
        :param loc_desc: loc_desc: 元素文本的描述(记录日志的时候使用)
        :param timeout: 最大等待事件
        :param poll_time: 等待的轮询间隔
        :return: 定位到的element
        """
        try:
            ele = WebDriverWait(self.driver, timeout, poll_time).until(
                EC.visibility_of_element_located(loc)
            )
        except Exception as e:
            log.error("等待-【{}】-元素可见超时".format(loc_desc))
            log.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            log.info("等待-【{}】-元素可见成功".format(loc_desc))
            return ele

    def wait_presence_ele(self, loc, loc_desc='', timeout=20, poll_time=0.5):
        """等待元素被加载
        :param loc: loc: 元素的定位器 -->:(BY.xxx,'表达式')
        :param loc_desc: loc_desc: 元素文本的描述(记录日志的时候使用)
        :param timeout: 最大等待事件
        :param poll_time: 等待的轮询间隔
        :return: 定位到的element
        """
        try:
            ele = WebDriverWait(self.driver, timeout, poll_time).until(
                EC.presence_of_element_located(loc)
            )
        except Exception as e:
            log.error("等待元素-【{}】--加载到页面-超时".format(loc_desc))
            log.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            log.info("等待元素-【{}】--加载到页面-可见成功".format(loc_desc))
            return ele

    def wait_ele_be_clickable(self, loc, loc_desc='', timeout=20, poll_time=0.5):
        """等待元素可点击
        :param loc: loc: 元素的定位器 -->:(BY.xxx,'表达式')
        :param loc_desc: loc_desc: 元素文本的描述(记录日志的时候使用)
        :param timeout: 最大等待事件
        :param poll_time: 等待的轮询间隔
        :return: 定位到的element
        """
        try:
            ele = WebDriverWait(self.driver, timeout, poll_time).until(
                EC.element_to_be_clickable(loc)
            )
        except Exception as e:
            log.error("等待元素-【{}】--可点击-超时".format(loc_desc))
            log.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            log.info("等待元素-【{}】--可点击-可见成功".format(loc_desc))
            return ele

    def get_element_text(self, loc, loc_desc=''):
        """
        获取元素的文本
        :param loc: 元素的定位器 -->:(BY.xxx,'表达式')
        :param loc_desc: 元素文本的描述(记录日志的时候使用)
        :return: 元素的text
        """
        try:
            text = self.driver.find_element(*loc).text
        except Exception as e:
            log.error("获取元素-【{}】--文本失败".format(loc_desc))
            log.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            log.info("获取元素-【{}】--文本成功".format(loc_desc))
            return text

    def get_element_attr(self, loc, attr, loc_desc=''):
        """
        获取元素的属性
        :param loc: 元素的定位器 -->:(BY.xxx,'表达式')
        :param attr: 元素的属性
        :param loc_desc: 元素文本的描述(记录日志的时候使用)
        :return: 元素的属性
        """
        try:
            text = self.driver.find_element(*loc).get_attribute(attr)
        except Exception as e:
            log.error("获取元素-【{}】--属性失败".format(loc_desc))
            log.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            log.info("获取元素-【{}】--属性成功".format(loc_desc))
            return text

    def get_element(self, loc, loc_desc=''):
        """
        查找元素
        :param loc: 元素的定位器 -->:(BY.xxx,'表达式')
        :param loc_desc: 元素文本的描述(记录日志的时候使用)
        """
        try:
            ele = self.driver.find_element(*loc)
        except Exception as e:
            log.error("查找元素-【{}】--失败".format(loc_desc))
            log.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            log.info("查找元素-【{}】--成功".format(loc_desc))
            return ele

    def click_element(self, loc, loc_desc=''):
        """
        点击元素
        :param loc: 元素的定位器 -->:(BY.xxx,'表达式')
        :param loc_desc: 元素文本的描述(记录日志的时候使用)
        :return:
        """
        try:
            self.driver.find_element(*loc).click()
        except Exception as e:
            log.error("点击元素-【{}】--失败".format(loc_desc))
            log.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            log.info("点击元素-【{}】--成功".format(loc_desc))

    def input_send_keys(self, loc, value, loc_desc=''):
        """
        往input中输入数据
        :param loc: input元素的定位器 -->:(BY.xxx,'表达式')
        :param value: 输入的值
        :param loc_desc: 元素文本的描述(记录日志的时候使用)
        :return:
        """
        try:
            ele = self.driver.find_element(*loc)
            ele.clear()
            ele.send_keys(value)
        except Exception as e:
            log.error("往input元素-【{}】--输入值失败".format(loc_desc))
            log.exception(e)
            self.page_save_screenshot(loc_desc)
            raise e
        else:
            log.info("往input元素-【{}】--输入值成功".format(loc_desc))

    def page_save_screenshot(self, loc_desc):
        """
        页面截图
        :param loc_desc:操作的描述
        :return:
        """
        try:
            # 获取当前时间，并转换为指定格式的字符串
            date_decs = time.strftime("%Y-%m-%d_%H_%M_%S")
            filename = date_decs + loc_desc + ".png"
            file_path = os.path.join(ERROR_IMAGE, filename)
            self.driver.save_screenshot(file_path)
        except Exception as e:
            log.error("对-【{}】--这个操作进行页面截图失败".format(loc_desc))
            log.exception(e)
            raise e
            log.info("对-【{}】--这个操作进行页面截图成功,图片保存为{}".format(loc_desc, filename))
        else:
            log.info("对-【{}】--这个操作进行页面截图成功,图片保存为{}".format(loc_desc, filename))
