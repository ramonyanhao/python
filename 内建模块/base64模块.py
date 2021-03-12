# Base64是一种用64个字符来表示任意二进制数据的方法
'''
base64就是把二进制数据先转换为base64中的64个字符，然后再把这些数据解码为字符串，base64并不是直接操作二进制数据
base64转换过后的数据字节为4的倍数，如果不够4的倍数则用=补齐
'''
# 处理去掉=的base64解码函数
import base64
def extra_part(n):
    k=len(n)%4
    if k>0:
        n+=b'='*(4-k) # 计算多出的部分是重点，因为base64解码长度必须是4的倍数，如果n的长度不是4的倍数计算多出的部分使用=补齐，这里使用4-len(n)%4得出不到4的倍数还差多少
        # 例如9不是4的倍数，但12是4的倍数，使用9%4=1,然后4-1=3，最后9+3=12
    return base64.b64decode(n)
print(base64.b64encode(b'abcd'),extra_part(b'YWJjZA'))

# struct的pack函数把任意数据类型变成bytes
import struct
print(struct.pack('>I', 10240099)) # >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数,H表示2字节无符号整数，c表示1字节无符号整数
# unpack把bytes变成相应的数据类型
print(struct.unpack('>I', b'\x00\x9c@c'))
# 可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数
import base64
f = open(r'图片存储路径','rb')    #以二进制方式读取位图文件
text = f.read()          # 将文件读取出来
def bmp_info(data):
    s=struct.unpack('<ccIIIIIIHH', data[:30]) # [:30]取前30字节
    print(s) # b'B'、b'M'说明是Windows位图，位图大小为164x164，颜色数为24
    return {
        'width': s[6],
        'height':s[7],
        'color': s[9]
    }
# 测试
bi = bmp_info(text)
print(bi)