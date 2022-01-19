import setting
import pg_list
import calculation
import sys


def main():
    """
    工具主程序
    """
    jc_value, yx_value = setting.check_setting()
    status = True
    while status:
        choice = pg_list.tool_list()
        if choice == '1':
            calculation.jc_calculation(jc_value)
        elif choice == '2':
            calculation.yx_calculation(yx_value)
        elif choice == '3':
            sys.exit()


if __name__ == '__main__':
    main()
