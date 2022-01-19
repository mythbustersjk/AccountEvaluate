"""
根据系统时间
"""
import datetime


def default_date():

    """
    根据当前系统月份自动生成月末日期
    :return:当前系统月份月末日期
    """

    month_a = ['1', '3', '5', '7', '8', '10', '12']
    month_b = ['4', '6', '9', '11']
    # 获取当前系统月份
    now_month = str(datetime.date.today().month)
    # 判断月末日期
    if now_month in month_a:
        real_date = str(datetime.date.today().year) + '-' + now_month + '-' + '31'
    elif now_month in month_b:
        real_date = str(datetime.date.today().year) + '-' + now_month + '-' + '30'
    elif now_month == '2':
        # 判断是否为闰年，根据结果判断月末日期
        now_year = datetime.date.today().year % 4
        if now_year == 0:
            real_date = str(datetime.date.today().year) + '-' + now_month + '-' + '29'
        else:
            real_date = str(datetime.date.today().year) + '-' + now_month + '-' + '28'

    return real_date


def default_quarterly():

    """
    判断系统当前日期所处季度，并自动返回季度末人日期
    :return: 当前季度末日期
    """

    Q1 = ['1', '2', '3']
    Q2 = ['4', '5', '6']
    Q3 = ['7', '8', '9']
    Q4 = ['10', '11', '12']

    q_month = str(datetime.date.today().month)
    # 季度判断
    if q_month in Q1:
        real_quarterly = str(datetime.date.today().year) + '-03-31'
    elif q_month in Q2:
        real_quarterly = str(datetime.date.today().year) + '-06-30'
    elif q_month in Q3:
        real_quarterly = str(datetime.date.today().year) + '-09-30'
    elif q_month in Q4:
        real_quarterly = str(datetime.date.today().year) + '-12-31'

    return real_quarterly


def default_yearly():

    """
    提供当前的年末日期
    :return: 当前年末日期
    """

    end_year = str(datetime.date.today().year) + '-12-31'
    return end_year
