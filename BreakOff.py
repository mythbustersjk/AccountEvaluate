import os


def cls():
    a = input("是否继续（'y‘ or ’n‘）")
    if len(a) == 0 or a == 'y':
        b = True
    else:
        b = False
        os.system('cls')
    return b
