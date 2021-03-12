def shellSort(arr):
    #n = len(arr)
    gap = int(n / 2)

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:#j=3,j-gap=1,34>2,下一轮循环54>3,j=4,j-gap=2,在进行一轮循环，j=2,arr[0]=12>temp,12>3满足条件
                arr[j] = arr[j - gap]#2=34 [12, 34, 54, 34, 3],下一轮循环arr[4]=arr[2],3=54[12, 2, 54, 34, 54]，下一轮循环arr[2]=arr[0],54=12,[12, 2, 12, 34, 54]
                j -= gap#3-2=1,j=1,下一轮循环4-=2，j=2,当j=2时还是满足while循环条件，j>=gap,这时的列表arr[0]>temp,12>temp,注意虽然列表发生了变化，最后的3变为54，可是temp变量再while循环外就已经赋值了，所以这个变量不会变，还是3，12>3
            arr[j] = temp#arr[1]=2,经过一次循环34和2更换了位置,arr[0]=3[3, 2, 12, 34, 54]
            print(arr)#gap=2时，循环最终列表为[3, 2, 12, 34, 54]
        gap = int(gap / 2)#gap=int(2/2)=1,符合while gap>0条件，循环开始，for i in range(1,5),temp=2,12,34,54,j=1,2,3,4.while 1>=1 and arr[1-1]>temp,arr[0]=3,temp=2,3>2符合条件循环开始
        #arr[j]=arr[j-gap],arr[1]=arr[0]2=3,[3, 3, 12, 34, 54],j-=gap,j=0,不符合循环条件j>=gap,循环结束，arr[j]=temp,arr[0]=temp,arr[0]=2[2, 3, 12, 34, 54]


arr = [12, 34, 54, 2, 3]

n = len(arr)
print("排序前:")
for i in range(n):
    print(arr[i]),

shellSort(arr)

print("\n排序后:")
for i in range(n):
    print(arr[i]),