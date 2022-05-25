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

class Queue(object):
    def __init__(self):
        self.first = None
        self.last  = None
        self.size = 0

    def print_queue(self):
        temp = self.first
        print('=================')
        while temp != None:
            print(temp.data)
            temp = temp.next

    def enqueue(self, data):
        new_node = Node(data)
        
        if self.size == 0:
            self.first = new_node
            self.last  = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return False

        temp = self.first
        self.first = self.first.next
        temp.next = None

        self.size -= 1
        return temp


    def pop(self):
        if self.size == 0:
            return False
        
        temp = self.first
        self.first = temp.next
        temp.next = None
        self.size -= 1
        return temp
    
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.print_queue()

    queue.dequeue()
    queue.print_queue()
