prime_number = [x for x in range(int(input('区间最小值：')), int(input('区间最大值：'))) if[]== [y for y in range(2, int(x ** 0.5) + 1) if x % y == 0]]
#if[]== [y for y in range(2, int(x ** 0.5) + 1) if x % y == 0]判断if[]后面的表达式生成列表是否为空列表，如果是则if条件达成，生成素数列表
#通过ifx%y==0判断x值是否可以整除y，如果可以整除则生成列表，如果不能整除则条件不达成，生成空列表，这样结果和前面的if[]条件达成，生成素数列表
print(prime_number)
