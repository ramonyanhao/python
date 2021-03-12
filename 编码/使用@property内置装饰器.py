class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
#通过set_score()方法来设置成绩，再通过一个get_score()来获取成绩
s=Student()
s.set_score(60)
print(s.get_score())
#如果想把类中的方法直接变成属性来调用，Python内置的@property装饰器就是负责把一个方法变成属性调用的，我们把这个类改为这样
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s=Student()
s.score=60
print(s.score)
s.score=90
print(s.score)
#@property通过getter和setter方法来实现的,我们可以把类中的方法变为只读属性，只要给方法指定getter,不指定setter就可以了，例如这样
class Student(object):

    @property#通过@property为birth指定getter
    def birth(self):
        return self._birth

    @birth.setter#通过@birth.setter为birth指定setter
    def birth(self, value):
        self._birth = value

    @property#这里只为age指定了getter,并没有指定@age.setter,所以age函数是只读属性，因为它的返回值在函数里已经计算出来了，age就是一个整数，所以调用时直接使用k.age,不需要k.age()
    def age(self):
        import datetime
        return datetime.datetime.today().year-self._birth
#上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来
#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样程序运行时就减少了出错的可能性。
k=Student()
k.birth=1985
print(k.age)
# 使用time计算年龄
import time
now_time=time.time() # 获取当前时间戳
my_bir=(1985,5,16,12,10,15,2,134,0) # 通过时间元组返回我生日的时间戳(年份1985，月份5，日期16，小时12，分钟10，秒15，星期2，从每年的1月1日开始的天数：134天，夏令时标识符：0代表不执行夏令时，夏令时就是比标准时快一个小时)
old_years=(now_time-time.mktime(my_bir))/(365*86400) # 根据时间戳计算年龄，一年有365天，每天有86400秒，365*86400表示一年有多少秒，再用相差的时间戳除每年的秒数得出年龄35岁
print(old_years)

