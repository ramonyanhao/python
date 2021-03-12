def use_logging(level):#带参数的装饰器
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":#显示等级为警告的日志名字
                print("%s is running" % func.__name__)
            elif level == "info":#显示等级为信息的日志名字
                print("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="warn")#@use_logging(level="warn") 等价于 @decorator
def foo(name='foo'):
    print("i am %s" % name)

foo()