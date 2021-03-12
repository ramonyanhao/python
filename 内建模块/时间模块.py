# datetime是Python处理日期和时间的标准库，使用print打印时间对象会输出标准格式，例如:
from datetime import datetime
t=datetime.now()
print(t) # 如果不用print输出的格式是datetime.datetime(2020, 5, 21, 18, 41, 2, 950850)
# datetime转换为timestamp使用timestamp
print(datetime.now().timestamp())
# timestamp转换为datetime使用fromtimestamp
print(datetime.fromtimestamp(datetime.now().timestamp()))
# timestamp也可以直接被转换到UTC标准时区的时间，使用utcfromtimestamp
print(datetime.utcfromtimestamp(datetime.now().timestamp()))
# str转换为datetime使用datetime.strptime()
print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))
# datetime转换为str使用datetime.strftime()
print(datetime.now().strftime('%a, %b %d %H:%M')) # %a代表周几，%b代表几月，%d代表几号，%H:%M代表小时和分钟
# datetime加减使用timedelta这个类
from datetime import timedelta
print(datetime.now() + timedelta(hours=10)) # 计算10小时后的时间
print(datetime.now() - timedelta(days=1)) # 计算昨天的时间
# 本地时间转换为UTC时间使用tzinfo可以给时间增加时区，一般tzinfo的值是None,所以要增加时区需要使用replace替换掉这个值
from datetime import timezone # timezone就是UTC时区，代表在UTC时间基础上加一个时间参数代表当地时区，例如:timezone(timedelta(hours=8))输出UTC+08:00
print(datetime.now(timezone(timedelta(hours=8)))) # tzinfo=timezone(timedelta(hours=8)会在时间后面显示+08:00代表时区
tn=datetime(2015,12,12,15,30) # 2015-12-12 15:30
print(tn.replace(hour=7,tzinfo=timezone(timedelta(hours=-8)))) # 也可以写成这种形式，但是如果不用datetime.now()，使用变量并指定日期就需要replace
# 使用replace和datetime.now有个区别，replace只是替换掉tzinfo的值,并不能像datetime.now一样修改时间，使用replace输出结果还是变量的时间，只在时间后面增加了时区
# 如果需要修改变量时间就需要在replace中加入参数hour,hour就是代表变量时间增加或者减少时差后的时间,例如变量时间时15:30,使用replace增加了时区显示-8,然后根据15-8=7得出hour=7
print(timezone(timedelta(hours=0))) # timezone为UTC时区
print(timezone(timedelta(hours=8))) # UTC时区+8小时
# 时区转换可以通过utcnow()拿到当前的UTC时间，因为utcnow不能带参数，所以不能像print(datetime.now(timezone(timedelta(hours=8))))那样使用
print(datetime.utcnow().replace(tzinfo=timezone.utc)) # 输出标准UTC时间，因为有replace(tzinfo=timezone.utc)所以后面带有时区+00:00
# 通过astimezone()将UTC转换时区为北京时间
print(datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
# 需要注意的一点不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如直接从北京时间转为东京时间，北京时间为+08:00,东京时间为+09:00
print(datetime.now(timezone(timedelta(hours=8))).astimezone(timezone(timedelta(hours=9))))
print(datetime.now(timezone(timedelta(hours=-10)))) # 注意使用timezone后，系统会自动根据提供的timedelta修改当前时间,这里使用-10代表返回前10个小时时间
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关，全球各地的计算机在任意时刻的timestamp都是完全相同的，因为在1970年计算时间的时候已经给时间戳加了时区
print(datetime.fromtimestamp(datetime.now().timestamp())) # 通过当前时间戳查看当地时间
print(datetime.utcfromtimestamp(datetime.now().timestamp())) # 通过当前时间戳查看UTC时间，由于都用同一个时间戳，转换的时区就不一样了，所以时间戳和时区无关

import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):

    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')

    tz=re.match(r'^\w+([+-]\d+)\:\d+$',tz_str).group(1) # 时区相差的小时数+7和-09

    tz_utc=timezone(timedelta(hours=int(tz))) # UTC时区

    dt_utc=dt.replace(tzinfo=tz_utc) # 把当前UTC时区对应的时间赋值给变量dt_utc

    return dt_utc.timestamp() # 转化为秒
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0,t1
# t1和t2是两个时区的时间，但他们的时间戳是一样的，所以时间戳和时区是没有关系的，t1和t2都是在UTC+00:00基础上计算出来的，t1UTC+7，那么UTC当前时间就是2015-6-1 01:10:30
# t2UTC-09,那么在UTC当前时间2015-6-1 01:10:30 -9就是t2,2015-5-31 16:10:30,他们的时间戳1433121030.0其实就是UTC为0的时间戳：2015-6-1 01:10:30,UTC+00:00
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0,t2
print(to_timestamp('2015-6-1 01:10:30', 'UTC+00:00'))
print('ok')
