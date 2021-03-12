from collections import namedtuple
#namedtuple，你不必再通过索引值进行访问，你可以把它看做一个字典通过名字进行访问，只不过其中的值是不能改变的
Friend = namedtuple("Friend", ['name', 'age', 'email'])
f1 = Friend('giga', 38, 'gaga@qq.com')
print(f1)
print(f1.age)
print(f1.email)
f2 = Friend(name='jjuu', email='eeee@qw.com', age=15)
print(f2)

name, age, email = f2
print(name, age, email)

#扑克牌创建
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
kinds = ['spades', 'hearts', 'clubs', 'diamonds']
PokerCard = namedtuple('PokerCard', ('card', 'kind'))
PokerCards = [PokerCard(card, kind) for card in cards for kind in kinds]
print(PokerCards)

#列表推导式
ca = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
ki = ['spades', 'hearts', 'clubs', 'diamonds']
ck=[(x,y) for x in ca for y in ki]
print(ck)