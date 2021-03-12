'''在cmd中调用test.py文件中的print_func函数，带world参数：python -c "import test;test.print_func('world')"'''
import profile
# profile和pstats是python代码的分析器,可以很客观查看代码的运行质量和使用的资源.在调试程序时有很大的帮助
def one():                #定义一个one函数

    sum=0
    for i in range(10000):
        sum+=i
    return sum

def two():
    sum=0
    for i in range(100000):
        sum+=i
    return sum

def there():
    sum=0
    for i in range(100000):
        sum+=i
    return sum

if __name__=="__main__":
    profile.run("one()","result.txt")      #将结果保存到result文件中
    profile.run("two()")
    profile.run("there()")
