def leftRotate(arr, d, n):
    print(arr)
    for i in range(gcd(d, n)):
        temp = arr[i]
        j = i
        while 1:
            k = j + d#k初始值为2，每次循环加2，2，4，6，8
            if k >= n:#当k的值为8时，大于n的值
                k = k - n#k=8-7，k第一次循环后的值为1，然后再回到k=j+d,由于下面指定了j=k,所以k又从1开始加2，加到7时k=7-7
            if k == i:#当k=0时退出循环
                break
            arr[j] = arr[k]#第一次循环k的值是2，j的值是0，arr[0]=1,arr[2]=3,这里把arr的0变为3，第2次arr[2]=3,arr[4]=5,再把3变为5，第3次arr[4]=5,arr[6]=7,把5变为7
            # 第4次注意k的值为8，符合条件k>=n,k=8-7，k的值为1，arr[6]=7,arr[1]=2,把7变为2
            print(arr)
            j = k
        arr[j] = temp
        print(j)
def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


arr = [1,2,3,4,5,6,7]
leftRotate(arr, 2, 7)
printArray(arr, 7)
print()
def play(arr,n):
    for i in range(n):
        arr.append(arr.pop(0))
        print(arr)
    return arr
print(play([1,2,3,4,5,6,7],2))