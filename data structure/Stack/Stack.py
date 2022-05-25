# coding=utf-8
"""
:Copyright: © 2022 Darren Liang, Inc. All Rights Reserved.

@Author: Darren Liang
@Date  : 2022-02-27
"""

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack(object):
    def __init__(self):
        self.top  = None
        self.size = 0

    def print_stack(self):
        temp = self.top
        print('=================')
        while temp != None:
            print(temp.data)
            temp = temp.next

    def push(self, data):
        new_node = Node(data)

        if self.size == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1
        return True

    def pop(self):
        if self.size == 0:
            return False
        
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.size -= 1
        return temp
    
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()

    stack.pop()
    stack.print_stack()
