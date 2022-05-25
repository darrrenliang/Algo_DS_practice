# coding=utf-8
"""
:Copyright: © 2022 Darren Liang, Inc. All Rights Reserved.

@Author: Darren Liang
@Date  : 2022-02-25
"""


class LinkedNode(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 
    
class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def print_list(self):
        # O(n)
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
        
    def appened(self, data):
        # O(1)
        new_node = LinkedNode(data)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.size += 1
        return True
    
    def pop(self):
        # O(1)
        if self.size == 0:
            return False
        
        temp = self.head
        prev = self.head
       
        while (temp.next):
            prev = temp
            temp = temp.next
            
        self.tail = prev
        self.tail.next = None
        self.size -= 1

        if self.size == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        #O(1)
        new_node = LinkedNode(value)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.size += 1
        return True

    def pop_first(self):
        
        if self.size == 0:
            return False

        temp = self.head
        self.head = temp.next
        temp.next = None
        self.size -= 1

        if self.size == 0:
            self.head = None
            self.tail = None
        return temp.data

    def get(self, index):
        if self.size == 0 or index > self.size:
            print("index out of range")
            return False
        
        temp = self.head
        for _ in range(index-1):            
            temp = temp.next

        return temp        

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.data = value
            return True
        return False

    def insert(self, index, value):
        
        if index == 0:
            return self.prepend(value)
        
        if index < 0 or index > self.size:
            print("Index out of range")
            return False
        
        if index == self.size:
            return self.appened(value)

        new_node = LinkedNode(value)
        prev = self.get(index-1)
        temp = prev.next

        prev.next = new_node
        new_node.next = temp
        
        self.size += 1
        return True    
        
    def remove(self, index):

        if index < 0 or index > self.size:
            print("Index out of range")
            return False

        if index == 0:
            return self.pop_first()

        if index == self.size:
            return self.pop()

        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.size -= 1
        return True

    def reverse(self):
        temp = self.head
        prev = None

        while temp != None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev
        

class Testing(object):
    def __init__(self):
        self.list = LinkedList()

    def append(self):
        print("append element: 2")
        self.list.appened(2)
        
        print("append element: 7")
        self.list.appened(7)
        
        print("append element: 1")
        self.list.appened(1)

        print("append element: 5")
        self.list.appened(5)

        print("append element: 8")
        self.list.appened(8)
        self.list.print_list()

    def pop(self):
        print("pop the last element")
        self.list.pop()
        self.list.print_list()
    
    def prepend(self):
        print("prepend element: 11")
        self.list.prepend(11)
        self.list.print_list()
    
    def pop_first(self):
        print("pop the first element")
        self.list.pop_first()
        self.list.print_list()

    def get(self):
        data = self.list.get(2)
        print("the index 2 data of list is: %s" % data)

    def set_value(self):
        print("set index 2 of data to 99")
        self.list.set_value(2,99)
        self.list.print_list()

    def insert(self):
        print("insert 88 into index 3 of list")
        self.list.insert(3,88)
        self.list.print_list()

    def remove(self):
        print("remove the index 3 of data from list")
        self.list.remove(3)
        self.list.print_list()
    
    def reverse(self):
        print("reverse the linked list")
        self.list.reverse()
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
    test.reverse()