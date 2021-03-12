class student():
    count=0
    # count是类变量
    #@staticmethod #如果在这里使用@staticmethod改为静态方法，实例化student1和student2会报错
    def __init__(self,age,name):
        self.age = age
        self.name = name
        student.count+=1
    # 访问实例变量(用self.age  self.name)
#类变量：可在类的所有实例之间共享的值（也就是说，它们不是单独分配给每个实例的）。
#实例变量：实例化之后，每个实例单独拥有的变量,比如student1和student2都是实例化后单独拥有变量self.age和self.name
#静态方法@staticmethod是无法访问实例变量的，但可以访问类变量;而类成员方法@classmethod也同样无法访问实例变量，但可以访问类变量
student1 = student(18,'hello')#这样可以实例化多个自己想要的结果，并且每个实例化都有各自的变量self.age和self.name
student2 = student(20,'world')
print(student1.name)
# 打印实例变量，输出hello
print(student2.name)
# 打印实例变量，输出world
print(student.count)
# 打印类变量，由于执行了两次student,student1和student2,count的值为2
