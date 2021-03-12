lower_range = int(input('Key in the lower range: '))
upper_range = int(input('Key in the upper range: '))

list_prime = []
num_prime = 0


# 定义一个函数来判断给定一个数n是否是质数，输入True（质数），False（合数）
def is_prime(n):
    decision = False

    for i in range(2, n):
        if n % i == 0:
            decision = False
            return decision
            break
        else:
            continue

    decision = True
    return decision


for i in range(lower_range, upper_range + 1):

    outcome = is_prime(i)
    if i <=1:
        print('0和1不是质数')
    elif outcome == True:
        list_prime.append(i)
        num_prime += 1
    else:
        continue

print(list_prime)
print(num_prime)