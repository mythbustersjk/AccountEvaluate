"""
为程序提供菜带服务
"""


def tool_list():
    print("本工具是用于计算基础户和有效户指标工具")
    print('请选择:\n1.基础户指标计算\n2.有效户指标计算\n3.退出')
    choice = input("请输入：")
    return choice


def jc_list():
    print("基础户指标计算工具")
    print('请选择:\n1.计算用户成为基础户所需天数\n2.计算客户成为基础户所需存款\n3.退出')
    jc = input("请输入：")
    return jc


def yx_list():
    print("有效户指标计算工具")
    print('请选择:\n1.计算用户成为有效户所需天数\n2.计算客户成为有效户所需存款\n3.退出')
    yx = input("请输入：")
    return yx
