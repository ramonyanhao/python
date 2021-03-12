from functools import wraps
def decorator_name(f):
    @wraps(f)#@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性
    def decorated(*args, **kwargs):
        if not can_run:#这里通过if not条件把can_run变成了一个开关
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated
@decorator_name
def func():
    return ("Function is running")

can_run = True#if not can_run=True就是can_run=False
print(func())#can_run=False执行Function is running

can_run = False#if not can_run=False就是can_run=True
print(func())#can_run=True执行Function will not run
#日志
def logit(func):
    @wraps(func)#说白了wraps作用就是保存之前装饰对象的属性,保证属性不丢失
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging
@logit#调用logit函数，addition_func=logit(addition_func)所以func函数在这里就变成了addition_func函数了
def foo(name='ramon', age=34, height=190):
    print("I am %s, age %s, height %s" % (name, age, height))
    return foo
foo()#只要foo函数里的参数都指定了值，或者有默认参数，并且函数里有return返回值，都可以使用函数赋值给变量
x=foo()
x()

