# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0 

import cmath

def get_para(para):
    """获取参数a, b, c的函数"""
    while True:
        try:
            number = float(input('请输入{}:'.format(para)))
            if para == 'a' and number == 0:
                print('a不能等于0!\n')
                continue
        except ValueError:
            print('请输入一个实数!\n')
            continue
        else:
            break
    return number

def solve(a, b, c):
    """解方程的函数"""

    d = b*b - 4*a*c
    if d < 0: # 复数解
        sol_1 = (-b + cmath.sqrt(d)) / (2*a)
        sol_2 = (-b - cmath.sqrt(d)) / (2*a)
    else: # 实数解
        sol_1 = (-b + d**0.5) / (2*a)
        sol_2 = (-b - d**0.5) / (2*a)
    print('方程的两个解为:\n{}\n{}'.format(sol_1, sol_2))

print('-'*60)
print('求解二次方程式 ax**2 + bx + c = 0 '.center(50))
print('-'*60)
print('请提供a, b, c的值(a, b, c为实数，a ≠ 0)'.center(50))
print('-'*60)

while True:
    a = get_para('a')
    b = get_para('b')
    c = get_para('c')
    solve(a, b, c)
    active = input('\n是否继续？(y/n): ')
    if active == 'n':
        break