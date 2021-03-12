def rverseArray(arr, start, end):#这个函数的意义就是把start和end值互换
    while (start < end):
        arr[start],arr[end]=arr[end],arr[start]
        start += 1
        end = end-1
def leftRotate(arr, d):
    n = len(arr)#这里的n是7
    rverseArray(arr, 0, d - 1)#这里循环一次rverseArrasy函数
    print(arr)#把1和2互换
    rverseArray(arr, d, n - 1)#这里从2开始，到6循环2次
    print(arr)#把3和7互换，4和6互换
    rverseArray(arr, 0, n - 1)#这里从0开始，到6循环3次
    print(arr)#2，3互换，1，4互换，7，5互换
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2)
print(arr)
#简单方法
list=[1,2,3,4,5,6,7]
def relist(l,d):
    for i in range(d):
        l.append(l.pop(0))#把列表第一个取出放到列表最后一位
    return l#这里如果加return l，后面调用这个函数时直接打印就能有结果，不用先运行这个函数，然后再打印list列表
relist(list,2)
print(list)
list1=[1,2,3,4,5,6,7]
def easy(arr,num):
    return arr[num:]+arr[:num]
print(easy(list1,2))
