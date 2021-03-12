class Node(object):
    """节点"""

    def __init__(self, item):
        self.item = item
        self.next = None  # 指向下一节点


class SingleLinkList(object):
    """单向链表"""

    def __init__(self):
        self.__head = None  # 头节点

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head  # 创建游标指向头节点
        while cur is not None:
            print(cur.item, end=' ')
            cur = cur.next
        print()  # 换行

    def add(self, item):
        """链表头部添加节点"""
        node = Node(item)  # 创建节点
        node.next = self.__head  # 新节点下个元素指向头节点
        self.__head = node  # 头节点指向新节点

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            index = 0
            while index < pos-1:  # 注意这里是pos-1
                index += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head  # 头节点
        pre = None  # 前一个节点
        while cur is not None:
            if cur.item == item:
                if pre is None:  # 首节点
                    self.__head = cur.next
                else:  # 中间节点（或尾节点）
                    pre.next = cur.next
                break
            # 链表继续后移
            pre = cur
            cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
kk=SingleLinkList()
kk.append([1,2,3,4])
print(kk.travel())