import pickle

#write向文件写入字符串，在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时如果电脑断电写入的内容将丢失，如果使用pickle.dump将直接把信息保存在硬盘文件中
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

#pickle模块是以二进制的形式序列化后保存到文件中（保存文件的后缀为”.pkl”），不能直接打开进行预览
pickle.dump(data1, output)

# 便于存储。序列化过程将文本信息转变为二进制数据流。这样就信息就容易存储在硬盘之中，当需要读取文件的时候，从硬盘中读取数据，然后再将其反序列化便可以得到原始的数据
#便于传输。当两个进程在进行远程通信时，彼此可以发送各种类型的数据。无论是何种类型的数据，都会以二进制序列的形式在网络上传送。发送方需要把這个对象转换为字节序列，才能在网络上传输；接收方则需要把字节序列在恢复为对象。
pickle.dump(selfref_list, output, -1)
output.close()

import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')
#pickle.loads()方法是直接从bytes对象中读取序列化的信息，pickle.load()是从文件中读取。
#pickle.loads(bytes_object, *,fix_imports=True, encoding=”ASCII”. errors=”strict”)
data1 = pickle.load(pkl_file)
pprint.pprint(data1)#pprint()模块打印出来的数据结构更加完整，每行为一个数据结构，更加方便阅读打印输出结果
print(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
print(data2)
pkl_file.close()