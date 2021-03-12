arr = [1,12,2, 11, 13, 5, 6,18,4,9,-5,3,11]

def insertionSort(arr):
    #从要排序的列表第二个元素开始比较
    for i in range(1,len(arr)):
        j = i
        #从大到小比较，直到比较到第一个元素
        while j > 0:
            if arr[j] < arr[j-1]:#这里注意arr[j]是arr[j-1]的前一位值
                arr[j-1],arr[j] = arr[j],arr[j-1]#也就是当j>0时，比如列表第2位是12，第3位是2，那这里表示如果arr[2]<arr[2-1],值互换，12变为2，2变为12
            j -= 1
    return arr
print(insertionSort(arr))