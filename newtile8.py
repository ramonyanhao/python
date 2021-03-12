import time

date =input("输入时间（格式如：20170404）:")
Tuple_1=()
struct_time = time.strptime(date,"%Y%m%d")
Tuple_1 =struct_time
a = Tuple_1[7]
print (Tuple_1)
print (type(Tuple_1))
print ("今年的第%d天" %a)
print ("今年的第%d天" %Tuple_1.tm_yday)#可以把时间元组里的9个值(tm_year=2019, tm_mon=12, tm_mday=9, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=343, tm_isdst=-1)对应前面tm分别提取出来


import datetime
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)