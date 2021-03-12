list1 = ['A','B','C']
dict1 = {}
for i in range(3):
    order = int(input('你要把'+list1[i]+'放在第几位？（请输入数字1,2,3)'))
    dict1[order] = list1[i]
print(dict1)

list1 = []
print (list1)
# 清空原本列表list1的元素
for i in range(1,4):
    list1.append(dict1[i])#这里重要，表示dict1的值是{3: 'A', 2: 'B', 1: 'C'},list1.append(dict1[i])表示向list1列表添加dict1[i]的值，那根据for i in range(1,4),i的值为1,2,3.
    # dict1[i]则代表dict1[1]对应的值是c,dict1[2]对应的值是b,dict1[3]对应的值是a,dict1后面的[1][2][3]不是索引，是字典中的键，根据这个键得出字典后面的值
print(list1)