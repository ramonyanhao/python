import re


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))#自定义分组value的值,matched是下面re.sub每次match的返回值,相当于re.match.group('value')
    print(matched)
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))#?P自定义分组名称为value,re.sub参数count默认会匹配所有符合条件的字符串，而re.search只会匹配第一个成功匹配的值，re.match只会从开头匹配，返回匹配成功的一个
# re.split和其他函数不一样的地方是最后得出的结果是除了匹配的值以外的内容，因为split要以查找的内容作为分隔符，例如：re.split('123','oo123pp456'),结果是[oo,pp456]
# re.split还有一个地方就是再分割的时候匹配式为()，代表以括号内的内容为分隔符，并且分组全部输出，例如re.split('(123)','oo123pp456'),结果是['oo','123','pp456']
# 另一个重要的知识点是再交互模式中如果不用print输出，遇到\n直接输出\n不会做换行，例如s="you're asking me out.that's so cute.what's your name again?"
# print(re.sub(r"(\.)", r"\1\n", s))结果是
# you're asking me out.
# that's so cute.
# what's your name again?
# 如果直接使用re.sub(r"(\.)", r"\1\n", s)结果是"you're asking me out\nthat's so cute\nwhat's your name again\n"
# x='this is is ok ok'如果字符串中is和ok重复两次，需要保留一个
# y= re.sub(r'(\w+)\s\1',r'\1',x)其中(\w+)匹配一个以上的包括下划线的任何单词字符,\s匹配任何空字符比如空格，\1表示前面(\w+)这个组
# 意思很明确，(\w+)\s\1只可以匹配到is is和ok ok,(\w+)匹配第一个is,\s匹配中间的空格，\1就是匹配和第一个一样的单词is,符合这些条件的只有is is和ok ok,然后再把匹配到的替换成第一组的字符串
'''
非贪婪操作符“？”，这个操作符可以用在"*","+","?"的后面，要求正则匹配的越少越好
>>> re.match(r"aa(\d+)","aa2343ddd").group(1)
'2343'
>>> re.match(r"aa(\d+?)","aa2343ddd").group(1)
'2'
>>> re.match(r"aa(\d+)ddd","aa2343ddd").group(1) 
'2343'
>>> re.match(r"aa(\d+?)ddd","aa2343ddd").group(1)
'2343'
'''