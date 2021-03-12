# collections是Python内建的一个集合模块，提供了许多有用的集合类
from collections import namedtuple
Point = namedtuple('坐标', ['x', 'y']) # namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
p = Point(1, 2) # 如果通过p=(1,2)这个元组来表示坐标，很难看出是用来表示一个坐标的
print(p.x,p.y)
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈,deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照传入的参数顺序在内部的dict依次查找
from collections import ChainMap
cla=ChainMap({'a':1,'b':2},{1:'ramon',2:'harmon','a':3,1:None})
print(cla['a'],cla[1],cla[2]) # 在ChainMap中，优先查找传入的第一个字典中的键值，如果第一个没有找到就从第2个找，如果两个字典中有重复的键则优先使用第一个字典中的键
# Counter是一个简单的计数器，例如统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
    print(c) # c就是一个字典
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        self.__dict__[key]=value
        OrderedDict.__setitem__(self, key, value)
l=LastUpdatedOrderedDict(3)
l[1],l[2],l[3],l[4]='a','b','c','d'
print(l)
