# 在程序运行的过程中，所有的变量都是在内存中，当程序运行完变量所占用的内存就被操作系统全部回收，通过序列化可以把内存中的变量放在磁盘上永久保存
# pickle只能用在python上，而且由于版本不同所运行的pickle也不同，如果想要在其他平台上通用只能使用json
# pickle其实可以理解成把字符串转化为bytes类型，反序列化就是把bytes转化为字符串类型，使用pickle.dumps和pickle.loads,如果使用读取和写入文件形式使用pickle.dump和pickle.load
# 为了能够在所有系统通用这种序列化，采用json格式，json使用方法和pickle一样，都是用json.dumps和json.loads序列化数据，如果使用读取和写入文件形式使用json.dump和json.load
# 但是如果需要序列化的数据是类形式呢，例如：
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
def student2dict(std): # 把Student类转化为字典，然后通过json的default参数把这个字典再序列化为json格式
# 默认情况下，json.dumps()方法不知道如何将Student实例变为一个JSON的{}对象,因此我们为Student专门写一个转换函数，再把函数传到json中即可
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict)) # default参数是把任意一个对象变成一个可序列为JSON的对象，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
# 还有另一种方法,使用类中的魔法方法__dict__这个字典类完成，这样就可以不需要创建转换函数student2dict(std)了，但是定义了__slots__的class是没有__dict__方法的
print(json.dumps(s, default=lambda obj: obj.__dict__))
# json反序列化一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
def dict2student(d): # 反序列化函数，把通过loads()方法转换出的dict对象字典转化为Student类实例
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}' # 这是一个json格式的对象
print(json.loads(json_str, object_hook=dict2student)) # 反序列化的Student实例对象
'''使用json时注意，json.loads的对象必须时字符串格式，而且这个字符串不能使用双引号，必须是单引号才可以解析出来，例如：
        a="{'a':1,'b':2}"
        json.loads(a)就会报错，如果改为：a=’{“a”:1,”b“:2}‘或者使用json.dumps(a)把a变为'"{'a':1,'b':2}"'
        json.loads(a)就可以成功解析成{“a”:1,”b“:2}
        另外还有一个help函数可以获取函数的参数和语法，例如help(json)就会列出json函数的语法和参数
        '''