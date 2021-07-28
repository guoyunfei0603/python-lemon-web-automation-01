"""
============================
Author:柠檬班-木森
Time:2020/8/6   20:19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import os

# 项目的根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试用例的目录路径
CASE_DIR = os.path.join(BASE_DIR, "testcases")

# 测试报告的目录路径
REPORT_DIR = os.path.join(BASE_DIR, "test_result/reports")

# 日志目录的项目路径
LOG_DIR = os.path.join(BASE_DIR, "test_result/logs")

# 用例数据的项目路径
DATA_DIR = os.path.join(BASE_DIR, "casedatas")

# 配置文件目录的路径
CONF_DIR = os.path.join(BASE_DIR, "conf")

# 错误截图存放的路径
ERROR_IMAGE = os.path.join(BASE_DIR, "test_result/error_images")
