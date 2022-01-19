import json


def check_setting():
    """
    检查程序配置文件
    :return: 基础户，有效户门槛值
    """

    filename = "setting.json"
    # 检测setting.json文件是否存在，不存在则指导用户创建该文件
    try:
        # 读取setting.json文件中的配置
        with open(filename) as read_file:
            value = json.load(read_file)
            jc_value = value['jc']
            yx_value = value['yx']
    except FileNotFoundError:
        # 创建setting.json文件
        with open(filename, 'w') as create_file:
            create_value = {'jc': input("请设置基础户日均门槛值（万元）："), 'yx': input("请设置有效户日均门槛值（万元）：")}
            json.dump(create_value, create_file)
            jc_value = value['jc']
            yx_value = value['yx']
    return jc_value, yx_value
