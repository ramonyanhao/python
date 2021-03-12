'''
在修复BUG时，习惯用print()把可能有问题的变量打印出来看看，但是print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息
所以用print()来辅助查看的地方，都可以用断言（assert）来替代，assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常
assert expression 当expression判断为False时才会触发异常，断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况
等价于：
if not expression:
    raise AssertionError
'''
import sys
assert ('win' in sys.platform), "该代码只能在 windows 下执行" # 如果符合条件则运行接下来的代码，如果不符合条件则输出后面的字符串:该代码只能在 windows 下执行
# assert ('linux' in sys.platform), "该代码只能在 Linux 下执行"
# 通过上面的断言判断当前运行的什么操作系统，然后接下来要执行的代码
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert:python -O 断言代替print.py
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
import logging
logging.basicConfig(level=logging.WARNING,filename='err.log') # filename把错误输出到文件err.log中，指定记录信息的级别，有debug，info，warning，error等几个级别
# 当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息
s = '0'
n = int(s)
logging.info('n = %d' % n)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
