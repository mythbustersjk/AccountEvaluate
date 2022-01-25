"""
工具内所有提示信息
"""
from colorama import Fore, init

import os


def days_warning_info():
    os.system('cls')
    init(autoreset=True)
    print("--------------")
    print(Fore.YELLOW + "！！！注意！！！")
    print(Fore.RED + "输入起止时间时，请按照%Y-%m-%d的格式录入")
    print(Fore.GREEN + '起始时间未录入时，程序将会以系统当前日期为默认起始时间')
    print(Fore.LIGHTMAGENTA_EX + '1.结束时间未录入时，程序将会以系统当前日期月末为默认起始时间\n2.输入q系统将会默认设置结束时间为季末\n3.输入y系统将会默认设置结束时间为年末')
    print("--------------")
