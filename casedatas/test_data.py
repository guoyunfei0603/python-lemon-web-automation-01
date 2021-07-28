
"""
============================
Author:小白31
Time:2020/12/20 15:34
E-mail:1359239107@qq.com
============================
"""
class LoginData():
    """
    登录的测试数据
    """
    # 正常登录
    login_pass_data = [
        {"title": "正常登录", "phone": "18684720553", "pwd": "python"}
    ]

    # 账号/密码为空
    login_data_is_none = [
        {"title": "密码为空", "phone": "18684720553", "pwd": "", "expected": "请输入密码"},
        {"title": "手机号为空", "phone": "", "pwd": "python", "expected": "请输入手机号"},
    ]

    # 密码错误
    login_pwd_error = [
        {"title": "密码错误", "phone": "18684720553", "pwd": "pyt21hon","expected":"帐号或密码错误!"}

    ]

class InvestData:
    """投资功能的用例数据"""
    # 投资成功
    success_data = [
        {'title': '投资成功', 'money': 200, 'expected': '投标成功！'}
    ]
    # 投资失败投标置灰  非100整数倍且大于100，非100整数倍且小于100，字母，符号
    error_data = [
        {'title': '输入金额非10的整数倍', 'money': 456, 'expected': '请输入10的整数倍'},
        {'title': '输入金额为字母', 'money': 'a', 'expected': '请输入10的整数倍'},
        {'title': '输入金额为特殊字符', 'money': '$', 'expected': '请输入10的整数倍'}
    ]
    # 投资失败弹框提示  负数100整数倍金额，0，空格，100整数倍且小于100,投标的金额大于标剩余金额，购买标的金额大于标总金额，投标金额大于可用金额
    error_popup_data = [
        {'title': '输入金额为负数', 'money': -10, 'expected': '请正确填写投标金额'},
        {'title': '输入金额为0', 'money': 0, 'expected': '请正确填写投标金额'},
        {'title': '输入金额为空格', 'money': ' ', 'expected': '请正确填写投标金额'},
        {'title': '输入金额为10的整数倍，但少于100', 'money': 50, 'expected': '投标金额必须为100的倍数'}
    ]