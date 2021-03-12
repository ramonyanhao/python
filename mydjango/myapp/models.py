from django.db import models

class Topping(models.Model):
    name=models.CharField(max_length=128,verbose_name='名字')#verbose_name修改admin管理页面中的字段名name为名字
    weidao=models.CharField(max_length=128,verbose_name='味道')#修改admin管理页面中的字段名weidao为味道
    class Meta:
        db_table = '浇头'#修改数据库中的表名myapp_topping为浇头
        verbose_name = '浇头名'#这里是修改admin管理页面整个表名toppings为浇头名
        verbose_name_plural = '浇头名'#如果是复数修改admin管理页面整个表名toppings为浇头名，复数也就是表中有多条数据

    def __str__(self):
        return self.name
class Pizza(models.Model):
    zhishi=models.CharField(max_length=128,db_column='类型')#db_column可以指定数据库列名，如果没有指定则使用zhishi作为列名
    toppings = models.ManyToManyField(Topping)
    def __str__(self):
        return self.zhishi
'''
ManyToManyField多对多关系字段和OneToOneField一对一关系字段区别就是多对多关系字段可以通过add添加多个对象来互相访问，例如:p1.toppings.add(t1)
一对一关系字段只能通过Pizza的实例指定某个Topping实例互相访问，例如Pizza中修改toppings=models.OneToOneField(Topping,on_delete=models.CASCADE,primary_key=True)
在实例化后就变成p1=Pizza(zhishi='good',toppings=t1),重点就是一对一必须指定toppings字段如果把toppings指定为t2,就会把原先的t1替换掉变为t2,这就是一对一关系
t1=Topping(name='mogu',weidao='xian')
t1.save()
t2=Topping(name='lajiao',weidao='la')
t2.save
p1=Pizza(zhishi='good')
p1.save()
p1.toppings.add(t1) 把t1添加到Pizzas对象p1中，也可以反过来添加:t1.pizza_set.add(p1)
t1.pizza_set.all()查看在pizza中有哪些对象添加了这个t1,也可以使用索引来查看例如:t1.pizza_set.all()[0]
p1.toppings.all()查看这个pizza的对象p1中包含了那些Topping对象,也可以使用索引来查看例如:p1.toppings.all()[0]
也可以直接通过Pizza创建Topping字段：p2=Pizza(zhishi='very good'),p2.save(),p2.toppings.create(name='jitang',weidao='haochi')
新创建的Topping字段jitang就默认在Pizza的p2对象中，如果正常执行需要分成两步:t3=Topping(name='jitang',weidao='haochi'),p2.toppings.add(t3)
exclude用来排除相关项目，比如两个Pizza拥有不相同的Topping，使用exclude可以把这个不相同的Topping排除，返回结果就是另一个不包含这个Topping的Pizza项目
p2.toppings.add(t1.t2,t3)由于p1只添加了t1,这里执行exclude：Pizza.objects.exclude(toppings=t2)返回结果就是p1对象，因为只有p2添加了t2,排除t2那就只有没有添加t2的p1了
如果Pizza.objects.exclude(toppings=t1)返回的结果就是空的，因为p2和p1都添加了t1
Pizza.objects.filter(toppings__name__startswith="mogu")查询所有Topping的name字段开头为mogu的对象都在哪些Pizza对象中
Pizza.objects.filter(toppings__name__startswith="mogu").count()统计共有多少个项目，Pizza.objects.filter(toppings__name__startswith="mogu").distinct()去掉重复的项目
t1.delete()删除在Topping中的t1对象数据，例如t1是mogu,执行delete后在Topping.objects.all()中就没有mogu这个值了，同样p1.delete()也是一样
t1.pizza_set.remove(p1)只删除t1在p1的关系，但不删除元数据,t4=p1.toppings.all()[1]通过索引[1]把Pizza的第2个对象的值和关系赋值给t4
在ForeignKey或ManyToManyField字段中如果指定related_name(反向名称)和related_query_name(反向查询名称)就可以替代_set,例如t1.pizza_set如果指定了related_name这里就直接用t1.反向名称
例如:common/models.py
class Base(models.Model):
    m2m = models.ManyToManyField(
        OtherModel,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        # 例如下面的子类ChildA的反向名称:common_childa_related,common就是%(app_label)s,childa就是%(class)s
        # ChildA的反向查询名称:common_childas,注意查询名称%(class)ss多一个s，%(app_label)s和%(class)s就是两个变量指定下面继承的子类和app的名称
        # 如果没有指定这两个名称，就需要使用默认的_set来获取数据，例如childa_set()和childb_set()
        # django默认使用查看表中数据的命令是Base.objects.all(),如果指定了base=models.manage(),命令就变为Base.base.all()
    )
    class Meta:#class Meta做为嵌套类，主要目的是给上级类添加一些功能，或者指定一些标准.
        abstract = True#把Base这个类变为抽象类，抽象类不会在数据库中产生表，如果被下面的子类继承，这个抽象类中的字段会自动继承到子类中，通常用于把一些公用的字段放在抽象类中，可以避免重复操作
                       #在这个嵌套类中还可以指定数据表名称，django默认的数据表名是common_base,如果指定了db_table = '表名',通过migrate产生的表名就是这个ab_table指定的表名
                       #嵌套类中还可以指定字段的升序和降序，使用ordering = ['字段名']根据指定的字段名给表中的数据进行升序，使用ordering = ['-字段名']进行降序
                       #verbose_name和verbose_name_plural可以指定到admin管理页面中为verbose_name的值，verbose_name_plural为复数形式，就是verbose_name的值后面+s
class ChildA(Base):
    pass

class ChildB(Base):
    pass
在给出一个中间模型时，ManyToManyField.through_fields决定使用中间模型的那些字段来自动地建立一个多对多的关系，ManyToManyField.through指定表示要使用的中间表的Django模型
例如:
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)
'''