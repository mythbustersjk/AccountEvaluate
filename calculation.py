import days

from formula import JcFormula, YxFormula

import pg_list

from colorama import Fore, init

import os

import BreakOff


def jc_calculation(jc_value):
    init(autoreset=True)
    jc_tool = True
    while jc_tool:
        os.system('cls')
        jc = pg_list.jc_list()
        if jc == "1":
            current_amount = input('请输入当前账户日均（万元）：')
            current_balance = input('请输入当前账户余额（万元）：')
            need_days = JcFormula(jc_value, current_amount, current_balance)
            print(Fore.BLUE + f'该客户将在{round(need_days.jc_need_days_formula())}天后成为基础户')
            jc_tool = BreakOff.cls()
        elif jc == "2":
            total_days, end_date = days.day_js()
            current_amount = input('请输入当前账户日均（万元）：')
            current_balance = input('请输入当前账户余额（万元）：')
            if len(current_balance) == 0:
                current_balance = 0
            need_found = JcFormula(jc_value, current_amount, current_balance, total_days)
            print(
                Fore.BLUE + f'该客户需要存入{round(need_found.jc_amount_formula() - float(current_balance), 2)}万元，'
                            f'方可在{end_date}成为基础户')
            jc_tool = BreakOff.cls()
        elif jc == "3":
            jc_tool = False
            os.system('cls')


def yx_calculation(yx_value):
    init(autoreset=True)
    yx_tool = True
    while yx_tool:
        yx = pg_list.yx_list()
        if yx == "1":
            current_amount = input('请输入当前账户日均（万元）：')
            current_balance = input('请输入当前账户余额（万元）：')
            need_days = YxFormula(yx_value, current_amount, current_balance)
            print(Fore.BLUE + f'该客户将在{round(need_days.yx_need_days_formula())}天后成为基础户')
            yx_tool = BreakOff.cls()
        elif yx == "2":
            total_days, end_date = days.day_js()
            current_amount = input('请输入当前账户日均（万元）：')
            current_balance = input('请输入当前账户余额（万元）：')
            if len(current_balance) == 0:
                current_balance = 0
            need_found = YxFormula(yx_value, current_amount, current_balance, total_days)
            print(
                Fore.BLUE + f'该客户需要存入{round(need_found.yx_amount_formula() - float(current_balance), 2)}万元，'
                            f'方可在{end_date}成为有效户')
            yx_tool = BreakOff.cls()
        elif yx == "3":
            yx_tool = False
            os.system('cls')
