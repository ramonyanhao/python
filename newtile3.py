astr = "hello world ,hhhh world heihei"
def myreplace (astr,oldstr,newstr):
    result=astr.split(oldstr)#.split根据oldstr为分隔符来把astr切片，成为['hello',',hhhh','heihei']效果等于删除world字符,这里注意hhhh前面的逗号不会被删除
    print(result)
    return newstr.join(result)#.join根据newstr为指定字符把result进行连接，成为hello job,hhhh job heihei这里注意join用法，.join后面()里为需要连接的元素列表，.join前面为指定字符
print(myreplace(astr,"world","job"))


def replace (astr,old,new) :#改用replace函数
    str=astr.replace(old,new)
    print(str)
    return str
print(replace(astr,"world","job"))