def deduplication(self, nums):#找出排序数组的索引
    for i in range(len(nums)):
        if nums[i]==self:
            return i
        i = 0
        for x in nums:
            if self > x:
                i += 1

        return i


print(deduplication(6, [1,3,5,6]))
def min():
    for i in range(3):
        globals()['part' + str(i)] = i#globals查看全局变量,locals查看局部变量,两者返回值都是字典形式
    print(part0)#这里使用globals是因为在函数里，如果直接使用for循环，不再min函数里，可以把globals改为locals
    print(part1)
    print(part2)
min()
def cc():
    global cat#global把cat局部变量改为全局变量，运行cc函数后就可以再函数外部访问cat这个变量
    cat = '123'
cc()
print(cat)
print(globals()["__name__"])
print(globals()["__file__"])
print(globals())