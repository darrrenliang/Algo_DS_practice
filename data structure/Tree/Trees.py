# coding=utf-8
"""
:Copyright: © 2022 Darren Liang, Inc. All Rights Reserved.

@Author: Darren Liang
@Date  : 2022-02-28
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return True
        
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True    
                temp = temp.left
            else:
                # if new_node.value > temp.value:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
            
    def contains(self, value):
        temp = self.root

        while temp != None:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True
        return False

    def get_min_value_node(self, current_node):
        while current_node.left != None:
            current_node = current_node.left
        return current_node

if __name__ == "__main__":
    tree = BinarySearchTree()
    # tree.insert(2)
    # tree.insert(1)
    # tree.insert(3)
    # print(tree.root.value)
    # print(tree.root.left.value)
    # print(tree.root.right.value)
    # print(tree.get_min_value_node(tree.root).value)

    tree.insert(47)
    tree.insert(21)
    tree.insert(76)
    tree.insert(18)
    tree.insert(27)
    tree.insert(52)
    tree.insert(82)
    print(tree.contains(27))
    print(tree.contains(17))
    print(tree.get_min_value_node(tree.root).value)
    

