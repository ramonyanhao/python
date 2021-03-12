# StringIO顾名思义就是在内存中读写str
# encoding=utf-8
from io import StringIO
f = StringIO()
f.write('hello')
print(f.getvalue()) # getvalue()方法用于获得写入后的str
f = StringIO('Hello!\nHi!\nGoodbye!')
print(f.getvalue())
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8')) # 写入的不是str，而是经过UTF-8编码的bytes
print(f.getvalue())
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read().decode('utf-8'))
# 需要注意的一点如果使用sio.getvalue()覆盖原值的，指针始终是指向0的位置例如：
sio = StringIO('abc')
print(sio.getvalue())
sio = StringIO('def') # def会覆盖前面的abc
print(sio.getvalue())
# 如果使用write方法则是在原有内容上追加新内容，例如：
sio1 = StringIO()
sio1.write('abc')
print('sio1',sio1.getvalue())
sio1.write('def') # def会追加到abc后面，结果为abcdef
print('sio1',sio1.getvalue())