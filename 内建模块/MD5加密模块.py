# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5，调用SHA1和调用MD5完全类似
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])  # salt是通过chr转换20个48到122随机整数为ASCII字符
        self.password = get_md5(password + self.salt) # 为了密码安全，把转换的ASCII字符也加入到password中进行md5加密，主要是为了防止黑客通过简单密码的md5值推算出密码
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
def login(username, password):
    user = db[username]  # 这里注意了，user是通过db字典得出的值为User()的类实例
    return user.password == get_md5(password+user.salt)  # user.password就是类User中的password属性
# 注意user.password是加过ASCII字符,这里需要验证密码正确需要在login函数的password参数也要加一样的ASCII字符，使用user.salt就可以加入一样的ASCII字符，然后通过get_md5做md5加密
# 还有一个地方需要注意就是不能使用user.password-user.salt,因为user.password加入user.salt后被md5加密过了，在user.password中是找不到user.salt字符的
# 所以只能通过md5加密login的password参数加一样的ASCII字符来验证密码是否正确
# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
# Hmac算法意义就是把salt加入到password中，只不过这个过程不需要我们写代码实现，可以通过hmac函数实现，例如把上面的salt改为标准的hmac算法，验证用户口令
import hmac
def hmac_md5(key,s):
    return hmac.new(key.encode('utf8'),s.encode('utf8'),'MD5').hexdigest() # 使用md5加密,MD5是单向计算特性，只能加密不能解密
class User():
    def __init__(self,username,password):
        self.username=username
        self.salt=''.join([chr(random.randint(54,122)) for i in range(20)])
        self.password=hmac_md5(password,self.salt)
def login():
    input_username = input('please input username：')
    input_password = input('please input password:')
    user=User(input_username,input_password)
    print(user.password,hmac_md5(input_password,user.salt))
    if user.password == hmac_md5(input_password,user.salt):
        return 'ok'
print(login())
# Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash
