class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            print(self,key) # self就是类实例化对象d,key就是d中的键，使用self[key]得出对应的值
            return self[key]
        except KeyError: # 如果Dict没有传入参数就会在这里捕获到KeyError错误，并把KeyError错误转为AttributeError错误
            raise AttributeError(r"'Dict' 对象没有属性 '%s'" % key)

    def __setattr__(self, key, value): # 给self增加属性的时候用setattr,例如已经指定了实例属性a和b,再指定key=value时用setattr
        self[key] = value

import unittest

class TestDict(unittest.TestCase):

    def test_init(self): # 测试init
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value') # 检查d.key是否和value相等

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d) # 检查属性key是否在d中
        self.assertEqual(d['key'], 'value') # 检查d[key]是否和value相等

    def test_keyerror(self): # 当Dict没有传入属性的时候，通过assertRaises检查是否会抛出getattr中的KeyError
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
            print(value)

    def test_attrerror(self): # 当Dict没有传入属性的时候，通过assertRaises检查是否会抛出getattr中的AttributeError
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self): # setUp()和tearDown()方法分别在每调用一个测试方法的前后分别被执行
        print('setUp...')

    def tearDown(self): # 设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码
        print('tearDown...')
if __name__ == '__main__':
    unittest.main() # 运行单元测试，也可以在命令行中运行python 单元测试.py或者python -m unittest 单元测试