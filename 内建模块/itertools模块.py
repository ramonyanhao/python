import itertools # itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算
natuals = itertools.count(5) # 因为count()会创建一个无限的迭代器，所以natuals会从5开始输出无限个自然数
natuals1 = itertools.count(1,2) # 从自然数1开始输出无限个奇数，因为后面的2代表跳过1个自然数
for i in itertools.takewhile(lambda x: x <= 10, natuals): # 如果使用takewhile函数就可以让natuals只输出小于等于10的自然数，不会无限循环输出
    print(i,end='\t')
print()
for i in itertools.takewhile(lambda x: x <= 10, natuals1):
    print(i,end='\t')
print()
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A', 3)
for i in ns:
    print(i)
print()
# cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')
c=0
for i in cs:
    print(i)
    c+=1
    if c > 2:
        break
print()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c,end='\t')
print()
# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
print()
# 还可以忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
for key, group in itertools.groupby('AaaBBBCCAAa',lambda x:x.upper()):
    print(key, list(group))

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1)
    pi_l = []
    for i in natuals:
        if i > 2 * N:  # 为什么要乘以2，因为取奇数后实际总量就是N的两倍，
            # 保证后面有足够的奇数取值
            break
        elif i % 2:
            pi_l.append(i)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    lenth = len(pi_l)  # 计算pi_l的个数

    pi_sum = 0  # 求和变量初始值
    pi_num = 0  # 标记用，用来结束循环
    for c in itertools.cycle([4, -4]):
        pi_sum += c / pi_l[pi_num] # c无限循环在4和-4两个数，第一次循环c=4,pi_l=[1,3,4,5,7,9,11,13,15,17,19],pi_num=0,pi_l[pi_num]=1,所以第一次循环是4/1=4.0
        # 第2次循环c=-4,pi_num=1,pi_l[pi_num]=3,-4/3=-1.3333333333333333,以此类推最后求和得出圆周率
        pi_num += 1
        if pi_num == lenth:
            break
    return pi_sum
def p(n):
# 通过一行代码计算圆周率
    return sum([4/i if i%4==1 else -4/i for i in range(1, 2*n, 2)]) # 先设定i的值在1到2*n之间的奇数，如果i%4=1用4/i,否则用-4/i
# 假如i为1，1%4=1,所以4/1=4.0,当i=3时，3%4=3，所以用-4/3=-1.3333333333333333,当i=5时，5%4=1,4/5=0.8,依次类推最后求和
# 另一种方法
def pi(N):
    return sum([(-1) ** (n - 1) * 4 / (n * 2 - 1) for n in itertools.takewhile(lambda i: i <= N, itertools.count(1))])
# 使用-1来确定最后值，先确定n的值时在1到N之间，N=10,n就是[1,2,3,4,5,6,7,8,9],(-1)**(1-1)*4/(1*2-1)=4,-1的零次方=1,当n=2时，(-1)**(2-1)*4/(2*2-1)=-1.3333333333333333
# 当n=3时，(-1)**(3-1)*4/(3*2-1)=0.8,因为-1的2次方就是两个-1相乘=1，-1的偶次方就是1，-1的奇次方就是-1,以此类推最后求和得出圆周率率，最重要的是弄清楚算法
