# coding=utf-8
"""
:Copyright: © 2022 Darren Liang, Inc. All Rights Reserved.

@Author: Darren Liang
@Date  : 2022-02-27
"""

class LinkedNode(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def append(self, data):
        new_node = LinkedNode(data)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return True

    def pop(self):
        if self.size == 0:
            return False
        
        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        temp.prev = None
        self.size -= 1

        if self.size == 0:
            self.head = None
            self.tail = None
        
        return temp
        

    def prepend(self, data):
        new_node = LinkedNode(data)

        if self.size == 0:
            return self.append(data)
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1
        return True

    def pop_first(self):
        if self.size == 0:
            return False
        
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        temp.next = None
        self.size -= 1

        if self.size == 0:
            self.head = None
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index > self.size:
            return False
        
        temp = self.head
        if index < self.size/2:
            print("from head of DLL")
            for _ in range(index-1):
                temp = temp.next
        else:
            print("from tail of DLL")
            temp = self.tail
            for i in range(self.size, index, -1):
                temp = temp.prev 
        return temp     

    def set_value(self, index, data):
        if index < 0 or index > self.size:
            return False
        
        temp = self.get(index)
        temp.data = data
        return True

    def insert(self, index, data):
        if index < 0 or index > self.size:
            return False
        
        if index == 0:
            return self.prepend(data)

        if index == self.size:
            return self.append(data)

        new_node = LinkedNode(data)
        before = self.get(index -1)
        after  = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev  = new_node
        self.size += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.size:
            return False
        
        if index == 0:
            return self.pop_first()
        
        if index == self.size:
            return self.pop()

        temp   = self.get(index)
        before = temp.prev
        after  = temp.next
        before.next = after
        after.prev  = before        
        temp.prev = None
        temp.next = None
        self.size -= 1
        return temp

class Testing(object):
    def __init__(self):
        self.list = DoubleLinkedList()

    def append(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.append(4)
        self.list.append(5)
        self.list.append(6)
        print("append 1~6 to DLL")
        self.list.print_list()
    
    def pop(self):
        print("pop the last element")
        self.list.pop()
        self.list.print_list()
    
    def prepend(self):
        print("prepend the element 99 to DLL")
        self.list.prepend(99)
        self.list.print_list()

    def pop_first(self):
        print("pop the first elemet from DLL")
        self.list.pop_first()
        self.list.print_list()

    def get(self):
        print("get the index 3 of data from DLL")
        node = self.list.get(3)
        print(node.data)

    def set_value(self):
        print("set the index 3 data to 0")
        self.list.set_value(3, 0)
        self.list.print_list()

    def insert(self):
        print("insert the data 88 into the index 4 of DLL")
        self.list.insert(4, 88)
        self.list.print_list()

    def remove(self):
        print("remove the index 3 of data in DLL")
        self.list.remove(3)
        self.list.print_list()


if __name__ == "__main__":
    test = Testing()
    test.append()
    test.pop()
    test.prepend()
    test.pop_first()
    test.get()
    test.set_value()
    test.insert()
    test.remove()