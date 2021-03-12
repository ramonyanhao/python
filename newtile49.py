import random
class computer(object):

    def __init__(self):
        pass

    g_num = 0
    def ger_num(start,end):
        return random.randint(start,end)

    def contrl(ctl_str):
        global g_num
        if ctl_str == 'l' or ctl_str == 'L':
            g_num -= 1
            if g_num < 0:
                g_num = 23
        elif ctl_str == 'r' or ctl_str == 'R':
            g_num += 1
            if g_num > 23:
                g_num = 0
        return g_num

    @staticmethod
    def print_space(space_num):
        print_content = ['-']*24
        print_content = ''.join(print_content)
        l_content = list(print_content)
        l_content[space_num] = '*'
        l_content = ''.join(l_content)
        print(l_content)

if __name__ == '__main__':
    #生成随机数，确定星号的位置
    g_num = computer.ger_num(0,24)
    computer.print_space(g_num)
    while True:
        ctrl_str = input("请输入移动星星的指令(L/l or R/r):")
        if ctrl_str == 'EXIT' or ctrl_str == 'exit':
            break
        g_num = computer.contrl(ctrl_str)
        computer.print_space(g_num)