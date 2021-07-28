"""
============================
Author:小白31
Time:2021/1/12 22:16
E-mail:1359239107@qq.com
============================
"""

# 无头浏览器模式运行,非GUI界面运行web自动化

from selenium import webdriver


# 无头模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# 禁用GPU（图形处理器）加快速度运行
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
driver.get('https://www.baidu.com')

driver.save_screenshot('baidu.png')
driver.quit()
