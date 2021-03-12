name='whole gloable'
class Person(object):
    def __init__(self, newPersonName):
        self.name = newPersonName
        '''
        此处正确的，通过访问self.name的形式，实现了：
            1.给实例中，增加了name变量
            2.并且给name赋了初值，为newPersionName
        '''

    def sayYourName(self):
        '''
        此处由于开始正确的初始化了self对象，使得其中有了name变量，
        所以此处可以正确访问了name值了
        '''
        print('My name is %s' % self.name)

Person('Tim').sayYourName()#用这个也可以调用Person类或者函数


def selfAndInitDemo():#或者创建新函数然后指定变量并调用
    personInstance = Person('Tim')
    personInstance.sayYourName()


if __name__ == '__main__':#当 .py 文件被直接运行时，if __name__ == '__main__' 之下的代码块将被运行； 当 .py 文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行
    selfAndInitDemo()
