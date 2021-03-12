'''
with open("text.txt") as f:
    for line in f.readlines()
　　　　print(line)
1.首先生成一个上下文管理器expression，在上面例子中with语句首先以“test.txt”作为参数生成一个上下文管理器open("test.txt")。

2.然后执行expression.__enter__()。如果指定了[as variable]说明符，将__enter__()的返回值赋给variable。上例中open("test.txt").__enter__()返回的是一个文件对象给f。

3.执行with-block语句块。上例中执行读取文件。

4.执行expression.__exit__(),在__exit__()函数中可以进行资源清理工作。上面例子中就是执行文件的关闭操作。
'''
# 并不是只有open()函数返回的文件对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self): # 在类中实现了__enter__和__exit__就可以把类对象用在with中
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()
# 编写__enter__和__exit__很繁琐，我们使用@contextmanager来替换掉他们
from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name
    def query(self):
        print('Query info about %s...' % self.name)
# 使用@contextmanager就可以不需要编写__enter__和__exit__方法了
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
with create_query('Bob') as q:
    q.query()
# 需要注意的地方是函数create_query使用yield生成器，在with中先执行函数create_query中yield上面的代码，当执行到yield q时，执行with语句中的代码q.query(),然后继续执行yield下面的代码
# 可以把函数中的yield就看成with语句下面执行的代码，如果希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield # 这里执行with中的代码
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
# closing()把对象变为上下文对象
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.baidu.com')) as page:
    print(page)
''''@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close() 由于closing有finally，所以肯定会执行thing.close(),注意的一点就是这个对象必须有close方法，否则finally执行会报错
        '''