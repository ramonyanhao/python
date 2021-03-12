def deduplication(nums):
    # write your code here
    exist_nums = {}
    pointer = 0
    for num in nums:
        if num not in exist_nums:
            exist_nums[num] = 'OK' #没有这句话exist_nums列表永远都是空的，给exist_nums空列表赋值后，
            # 第2轮循环时if num not in exist_nums检查到重复的数字已经在列表中则条件为false,if条件结束，for条件开始下一轮循环
            nums[pointer] = num
            print (num)
            print (exist_nums)
            pointer += 1
            print(pointer)
    return pointer  #返回pointer函数的最终结果：6
print(deduplication([1,1,1,1,1,1,2,2,2,2,2,2,2,2,33,4,10,11,100]))
