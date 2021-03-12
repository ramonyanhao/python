def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1#这里注意，不管下面的j值如何更改，到这里会重新给j赋值
        print(arr,j)
        while j >= 0 and key < arr[j]:

            arr[j + 1] = arr[j]#arr[j]按照列表顺序往后移一位，例如j为2时，arr[2]=13,这里运算后arr[j+1]=13,arr[2+1]=13,把13移动到arr[3]的位置

            j -= 1#控制语句，否则while会无限循环

        arr[j + 1] = key#这时的j为-1,因为while里j-=1,这里再把arr列表的索引+1就是arr[0]=key
        print(arr,j)

#最后for循环遍历完4次列表结束，in range(1,4)



def aa():

    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    print("排序后的数组:")
    for i in range(len(arr)):
        print("%d" % arr[i])
aa()