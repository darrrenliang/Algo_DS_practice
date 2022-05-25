# coding=utf-8
"""
:Copyright: © 2022 Darren Liang, Inc. All Rights Reserved.

@Author: Darren Liang
@Date  : 2022-03-01
"""

class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size
    
    def _hash(self, key):
        my_hash = 0

        for c in key:
            my_hash += (ord(c) * 23)
        return my_hash % len(self.data_map) 

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f"{i} : {val}")

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self._hash(key)
        if self.data_map[index] != None:
            for i in range(len(self.data_map)):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] != None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
        

if __name__ == "__main__":
    table = HashTable()
    table.set_item('bolts', 1400)
    table.set_item('washers',50)
    table.set_item('lumber', 70)
    table.print_table()

    print(table.get_item('washers'))
    print(table.keys())