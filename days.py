import datetime

import DateInitialization

import warning_info

from colorama import Fore, init


def day_js():
    """
    根据输入的起止日期计算相差天数
    :return: 起止日期相差天数（days），结束天数（end_date）
    """

    status = True
    while status:
        # 字体颜色自动重置
        init(autoreset=True)
        warning_info.days_warning_info()
        begin = input("请输入计算起始天数（2020-01-01）：")
        # 未输入起始天数的情况下，以系统当前日期作为默认值
        if len(begin) == 0:
            begin = datetime.datetime.now().strftime('%Y-%m-%d')
            print(Fore.RED + f'您未输入相关日期，系统以{begin}作为默认值')
        end = input("请输入计算结束天数（2020-01-02）：")
        # 未输入起始天数的情况下，以系统当前月末作为默认值
        if len(end) == 0:
            end = DateInitialization.default_date()
            print(Fore.RED + f'您未输入相关日期，系统以{end}作为默认值')
        elif end == 'q':
            end = DateInitialization.default_quarterly()
            print(Fore.RED + f'结束日期已设为{end}')
        elif end == 'y':
            end = DateInitialization.default_yearly()
            print(Fore.RED + f'结束日期已设为{end}')
        # 将输入的日期字符串转换格式为日期
        first_date = datetime.datetime.strptime(begin, '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d').date()
        # 计算相差天数
        days = (end_date - first_date).days
        # 相差天数判断，相差天数大于0 则返回相差天数。否则，让用户重新输入日期。
        if days > 0:
            return days, end_date
        else:
            print('结束日期小于开始日期或日期输入错误，请重新输入')
