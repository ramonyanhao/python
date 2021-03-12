import pandas as pd
import csv
import json
# 一般先使用pandas读取文件内容再转化为数组，然后交给numpy处理这个数组array
# JSON：是一种轻量级的数据存储格式，用来保存数据，键值对存放，键必须唯一，值可以是任意类型,josn里面的内容需要双引号否则报错，例如：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
# CSV: 以纯文本的形式存储表格数据。该文件是一个字符序列，可以由任意数目的记录组成，记录间以某种换行符分割。每条记录由字段组成，字段间的分隔符是其他字符或者字符串。所有的记录都有完全相同的字段序列，相当于一个结构化表的纯文本形式
# 一般csv用来读取csv文件内容，如果要读取一个数据对象如csv_data可以使用pandas
with open('test.csv', 'w', encoding='utf8') as myFile:  # 写csv文件
    myWriter = csv.writer(myFile)
    myWriter.writerow(['id', 'name', 'sex', 'age'])
    myList = [[1, 'wang', '男', 18], [2, 'li', '女', 17], [3, 'zhao', '男', 20]]
    myWriter.writerows(myList)
with open('test.csv', 'r', encoding='utf8') as myFile:  # 读取csv文件
    lines = csv.reader(myFile)
    print(list(lines))
# 使用pandas来操作csv格式
csv_data = {'姓名': ['wang', 'li', 'zhao'], '年龄': [18, 20, 30], '性别': ['男', '女', '男']}
df = pd.DataFrame(csv_data)  # pandas使用DataFrame读取csv数据对象,如果读取csv文件使用pd.read_csv
print(df)
print(df.loc[0], df.loc[:2])  # 按照索引读取第一行数据,索引为[:2]访问多行数据
print(df.iloc[0], df.iloc[:2])  # iloc是实实在在的第几行数据，不是按照索引读取的
print(df.sort_values(['年龄']))  # 按照年龄排序
print(df.年龄, df[['姓名', '年龄']])  # 取出年龄一列的数据，还有一种方法是df['年龄']也可以取出,有一点不同是如果想要取出多列数据，可以通过df[['姓名', '年龄']]来获取，注意双中括号
df_values, df_value_counts = df.values, df.年龄.value_counts()  # 重点是这里，这里返回的是csv中所有的值组成的数组,可以通过values返回的数据交给numpy处理,value_counts()用来统计年龄阶段有多少个人
print('value:%s' % df_values, 'value_count:%s' % df_value_counts)
print(df.年龄 * 2)  # 可以对int类型的数据列进行计算
print(df.drop(0, axis=0))  # 去掉第一行数据，axis=0是指行，0是索引号
print(df.drop('姓名', axis=1))  # 去掉姓名那一列的数据，axis=1是指列，列名是姓名
print(df[df.年龄 > 18])  # 返回年龄大于18的数据
print(df.年龄 > 18)  # 返回值为True或者False
# 也可以使用map给df添加一列数据,map()的功能是将一个自定义函数作用于Series对象(df.年龄)的每个元素
def func(age):
    if age <= 20:
        return '青少年'
    elif age > 20:
        return '青年'
df['年龄分类'] = df.年龄.map(func)  # 增加一列数据名为年龄分类
# 添加一行数据:df.loc[索引] = [对应的列值],添加多行数据:df.append({'列名':列中的值,'列名':列中的值1},ignore_index=True)，ignore_index设置为True可以重新排列索引
# apply()函数的功能是将一个自定义函数作用于DataFrame的行或者列
df['年龄'] = df.年龄.apply(lambda x: x + 10)  # 给年龄增加10岁,pandas需要特别注意:pandas中不会主动修改里面的数据，如果需要修改数据就需要指定数据的位置，例如指定了df['年龄'] = df.年龄.apply(lambda x: x + 10)
print(df)  # 如果没有指定df['年龄'],而是直接运行了df.年龄.apply(lambda x: x + 10),然后print(df)它还是输出原来的df,并不会给年龄增加10,只有指定了df['年龄']pandas才会修改原来的数据
# applymap()函数的功能是将自定义函数作用于DataFrame的所有元素
df = df.applymap(lambda x: str(x) + ' ==')  # 匿名函数中的x就是dataframe中的每一个数据，然后转换成字符串格式并且增加==
print(df)  # 由于直接运行df.applymap(lambda x: str(x) + ' ==')并不会给每个数据增加==,想要更改所有数据就需要指定df这个对象了
ad = pd.read_csv('test.csv')  # pandas读取csv格式的文件,如果读取excel格式文件使用pd.read_excel
# df.drop(index, axis=0) 去掉某一行数据，axis=0是指行，index是索引号
# df.drop(col_name, axis=1)   去掉某一列的数据，axis=1是指列，col_name是列名
# df.sum(axis=0)，是求每列的数据之和
# df.sum(axis=1)，是求每行的数据之和
# 使用pandas写入csv文件,字典中的key值即为csv中列名
dataframe = pd.DataFrame(csv_data)
# 将DataFrame存储为csv,index表示在保存的文件中是否显示行名，default=True,sep为分隔符
dataframe.to_csv("to_test.csv", index=False, sep=',')
# 将DataFrame存储为excel文件
dataframe.to_excel("to_test.xls", index=False)
