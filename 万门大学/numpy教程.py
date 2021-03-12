import numpy as np
import pandas as pd
# numpy是处理数组的，列表可以存储任意类型的数据，数组只能存储一种数据格式
df = pd.read_csv('test.csv')
df_array = df.values  # 把test.csv文件中的值转换为数组
print(type(df_array), df_array)  # numpy的数组类型是numpy.ndarray
print(type(np.zeros(10, dtype=int)), np.zeros(10, dtype=int))  # 产生10个整数类型元素的数组，默认是float类型,每个元素的值是0
print(np.ones((4, 4), dtype=float))  # 生成一个4*4的小数类型的数组，每个元素为1
print(np.full((3, 3), 3.14))  # 使用full可以指定生成每个元素的值为3.14的3*3的二维数组
print(np.full((3, 3, 4, 3), 3.14), np.ndim(np.full((3, 3, 4, 3), 3.14)))  # 生成3*3*4*3的四维数组，有3个数组，每个数组中又有3个数组，每个数组中有3列4行的数据
# np.zeros,np.ones,np.full都有like,like就是生成的数组格式和指定的对象一样，例如:
a = np.random.randint(0, 10, (3, 3))  # 3*3的从0到10的随机数组
print(np.full_like(a, 4.15))  # 生成了一个和a一样的3*3的数组，元素的值是4.15,np.zeros和np.ones用法和这个一样
print(np.random.random((3, 3)))  # 生成3*3的随机数类型的数组
print(np.random.randint(0, 10, (3, 3)))  # 生成3*3的随机类型为整数的数组
print(np.arange(0, 10, 2))  # 生成0到10，步长为2的数组
print(np.linspace(0, 3, 10))  # 范围取值,比arange好用，如果不知道步长多少，可以使用linspace取出0到3之间的随机10个数字
print(np.eye(3))  # 生成3*3的数组
print(a, a[0][2], a[0, 2])  # 访问数组中的元素,在numpy中，使用索引访问[0][2]和[0,2]效果一样
print(a, a[:2, :2])  # 取出数组前两行数据中的前两个元素，注意不能使用a[:2][:2]这样访问，因为a[:2]取出前两行数据并返回成一个新的数组，后面的[:2]就在这个新生成的数组上操作，返回的结果还是a[:2]
print(a.ndim, a.shape, a.size)  # ndim是数组的维度，这里是2维数组，shape是数组的格式，几乘几大小，size是数组的尺寸，一共有多少个元素
print(a.itemsize, a.nbytes)  # itemsize是数组中的每个元素占内存的多少个字节，nbytes是一共占用多少字节，例如这里每个元素是4个字节,一共占用了36个字节，代表了一共有9个数
# numpy数组的运算
print(a + 10)  # 给a数组中的每个元素都加10
print(np.sum(np.array([[1, 2], [3, 4]])))  # 多维数组求和使用np.sum会把数组中所有元素相加返回总数
print(np.sum(np.array([[1, 2], [3, 4]]), axis=1))  # 如果后面加参数axis=1代表只把数组中的行进行相加，axis值为1是对数组中的行做操作
print(np.sum(np.array([[1, 2], [3, 4]]), axis=0))  # 如果后面加参数axis=0代表只把数组中的列进行相加，axis值为0是对数组中的列做操作
print(a, a[a > 3], np.all(a > 0), np.any(a > 0))  # a[a>3]取出数组中所有大于3的数字,np.all和np.any都可以用来查看是否数组中的所有元素都是大于0的数字
# notebook中可以使用%timeit来测试代码的运行效率，返回代码最快的运行时间，可以用来做代码比较
print(a.reshape(1, 9))  # 给数组变形,a共有9个元素，是一个3*3的二维数组，现在把a变为1*9的二维数组
print(a, np.sort(a, axis=1), np.sort(a, axis=0))  # 给数组的行中按照每个元素大小做排序,如果按照数组中的列做排序，注意是按照数组中每列的第一个元素的大小做排序，如果第一个元素相等，就按照第二个元素大小排序
print(np.random.rand(100, 4).cumsum(0))  # 生成100行4列范围是0到1之间随机数的二维数组，cumsum(0)计算轴向元素累加和，0表示axis=0,按照行累加
