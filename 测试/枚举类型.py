# 在没有专门提供枚举类型的时候我们是怎么做呢，一般就通过字典或类来实现
# 但是通过字典或者类实现枚举类型，他们的值是可以更改的，所以更好的方式是使用标准库提供的 Enum 类型，使用Enum枚举类型最重要的原因就是它里面的值是不允许更改的
from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3
# 枚举的成员可以通过 is 同一性比较或通过 == 等值比较
print(Color.red is Color.red)
print(Color.red is not Color.blue)
print(Color.blue == Color.red)
print(Color.blue != Color.red)

# Color.red=5 枚举类型不可实例化，不可更改
# 定义枚举时，成员名不允许重复
# 成员值允许相同，第二个成员的名称被视作第一个成员的别名
# 若要不能定义相同的成员值，可以通过 unique 装饰
from enum import Enum, unique
@unique
class Color(Enum):
    red = 1
    green = 2
#   blue = 1 这里产生错误，使用unique后枚举类中不允许有重复的成员值
# 枚举成员不能进行大小比较,如果想要做大小比较，就需要扩展枚举 IntEnum
# IntEnum 是 Enum 的扩展，不同类型的整数枚举也可以相互比较：

from enum import IntEnum
class Shape(IntEnum):
    circle = 1
    square = 2

class Request(IntEnum):
    post = 1
    get = 2

print(Shape.circle == 1)            # True
print(Shape.circle < 3)             # True
print(Shape.circle == Request.post) # True
print(Shape.circle >= Request.post) # True