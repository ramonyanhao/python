class Student(object):
    __slots__ = ('name', 'age','f','score') # __slots__变量限制该class实例能添加的属性,注意是在类外的实例添加属性，如果方法或者属性在内部就没关系了，例如类变量k和方法inner
    k=123
    def inner(self):
        return self.k
s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
print(s.name,s.age,s.k,s.inner())
def f(self,score): # 动态语言的好处，可以在程序运行期间添加功能
    self.score=score
from types import MethodType
s.f=MethodType(f,s) # 给单实例s绑定f方法
s.f(10)
print(s.score)
Student.f=f # 给整个类绑定f方法，从而所有Student实例化对象都可以调用这个方法
s1=Student()
s1.f(2)
print(s1.score)
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是没办法检查参数，导致可以把成绩随便改:
s2=Student()
s2.f(9999)
print(s2.score)
Student.name='Harmon' # 也可以给整个类绑定其他属性供所有类实例调用，只要这个属性在__slots__中
Student.score=35
print(s1.name,s2.name,s1.score,s2.score)
# 我们使用@property来把类下面的方法变为像属性那样调用
class student:
    #__slots__ = ('_name', '_score')
    @property
    def student_name(self):
        return self._name
    @student_name.setter
    def student_name(self,name):
        if not isinstance(name,str):
            print('type error')
        self._name=name
    @property
    def student_score(self):
        return self._score
    @student_score.setter
    def student_score(self,score):
        if not isinstance(score,int):
            for i in score: # 如果需要传多个参数，比如传值一个列表或元组
                if not isinstance(i,int):
                    raise ValueError('type error')
                if i < 0 or i > 100:
                    raise ValueError('score must between 0~100')
        elif score<0 or score>100:
            raise ValueError('score must between 0~100')
        self._score=score

ramon=student()
ramon.student_name='ramon' # 这里注意使用property装饰器后，给student_name方法赋值使用=,不是像普通函数那样传值用()
ramon.student_score=[90,80,100] # 如果使用ramon.student_score(95)这样传值会报错
print(ramon.student_name,ramon.student_score)