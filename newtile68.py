def countSort(arr):
    output = [0 for i in range(256)]

    count = [0 for i in range(256)]

    ans = ["" for _ in arr]

    for i in arr:
        count[ord(i)] += 1
#更改count列表，把arr字符串所有字母对应的asci转换为数字后变为count的索引，再加1


    for i in range(256):
        count[i] += count[i - 1]
#计算count列表所有的数字和，计算后就可以把这个当作output列表的索引

    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]#这里最关键，按照上面count列表的索引找出再count列表对应的值，比如w,ord('w')=119,
        #count[119]对应的值是12，output[12-1]=output[11]=arr[i],所以output[11]=w,最终结果就是output列表里第11个0变为字母w,因为索引从0开始，所以这里要-1
        count[ord(arr[i])] -= 1#output列表通过count列表当索引找到一个字母后，这里就表示count列表索引减1，下次循环再通过count列表当索引时，
        #如果还找到w，按照刚才计算，count[119]所对应的值就变为11了，output[11-1]=arr[i]，output[10]=w,最终结果就是按照字母排序顺序把arr输出
        #继续运算字母r,ord('r')=114,count[ord('r')]=8,output[8-1]=arr[i],output[7]=r
    print(output)
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


arr = "wwwrunoobcom"
ans = countSort(arr)
print("字符数组排序 %s" % ("".join(ans)))