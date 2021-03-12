def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]#pivot就是每次比较列表中间的一个数
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)#这里注意用了left和right函数递归，arr列表比较完后，还要再把分开的left和right再做比较
print(quicksort([3, 6, 8, 19, 1, 5]))  #quicksort函数参数arr到函数递归时改为left和right,表示再把筛选过后的left和right再做一次函数运算


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = int (len(lst)/2)

    left = merge_sort(lst[ :middle])#和上面的函数递归一样，这里把函数参数lst改为lst[:middle],最终结果这里只会有一个数字赋值给left
    print(left)
    right = merge_sort(lst[middle: ])#右边
    merged = []
    while left and right:
        merged.append(left.pop(0) if left [0] <= right[0] else right.pop(0))
    merged.extend(right if right else left)  #该方法没有返回值，但会在已存在的列表中添加新的列表内容
    return merged
data_lst = [6,202,100,301,38,8,1]
print(merge_sort(data_lst))