#计算斐波那契数列，通过递归调用来实现,由于递归占用较多资源，对于大规模的计算消耗比较大，运算比较慢。反而通过循环实现的运算较快
def naqi(i):
    a = 0
    b = 1
    while i>0:
        a,b=b,a+b
# 最后返回的list都是i减到0,当i直接等于0时跳过while循环直接返回a,b值0和1,当i等于1时执行循环0,1=1,0+1得出a=1,b=1
# 当i等于2执行循环0,1=1,0+1得出a=1,b=1,i再减1，在之前得出的结果上再计算a,b=b,a+b:1,1=1,1+1得出a=1,b=2，i再减1等于0跳出while循环，return返回a和b的值a=1.b=2

        i-=1#i-=1在while循环里，代表当i>0时计算a,b，一直i-1到i<0结束循环
    return a,b,i
import time
current=time.process_time()
for i in range(10):
    print(naqi(i),end=' ')
now=time.process_time()
run=now-current
print('运行时间%f'%run)
print('='*20)
L = [0,1]#计算斐波那契数列，通过循环来实现
num = int(input("请输入你要的项数："))
if(num <= 0):
  print("请输入一个正整数！");
elif(num <= 2):
  if(num == 1):
    print("数列是：0")
  else:
    print("数列是：0,1")
else:
  for i in range(2,num):
    f = L[i-1] + L[i-2]#这里的i-1和i-2代表列表L的索引，比如，当i=2,f=L[2-1]+L[2-2]算出f的值时L列表的第2个值1+L列表的第一个值0,结果当i=2时，f=1
    L.append(f)
  print("数组是：")
  print(L)