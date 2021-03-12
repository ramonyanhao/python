import sys


def zero():
    return "zero"


def one():
    return "one"


def two():
    return "two"


def str_num(arg):
    # 注意字典中的键是数字格式，通过sys.argv[1]传进来的值是字符串格式，所以需要转换为数字格式才可以取出字典中的值
    switcher={
        0:zero,
        1:one,
        2:two,
        3:lambda:"three"
    }
    func = switcher.get(arg,lambda:"nothing")
    # 由于字典中的值都是函数，这里创建一个函数func,最后返回func()函数的运行结果,也可以直接 return switcher.get(arg,lambda:"nothing")()
    # 这里有个重点，在switcher字典中，使用get按照传进来的参数arg取出字典中的值，如果后面加入匿名函数lambda:"nothing",即使传入的arg在字典中找不到也不会返回None
    # 直接返回这个匿名函数的值nothing，这样做就很方便的把动态传进来的参数区分开
    return func()


if __name__ == '__main__':
    if sys.argv[1] == 'zero':
        print(zero())
    elif sys.argv[1] == 'one':
        print(one())
    elif sys.argv[1] == 'two':
        print(two())
    else:
        print(str_num(int(sys.argv[1])))
