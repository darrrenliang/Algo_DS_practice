# coding=utf-8
"""
:Copyright: © 2022 Advanced Control Systems, Inc. All Rights Reserved.

@Author: Darren Liang
@Date  : 2022-03-05
"""

LIST = [4, 2, 6, 5, 1, 3]

def InsertionSort(array):
    # start from second item.
    for i in range(1, len(array)):
        temp = array[i] 
        # print(temp)
        j = i -1
        while j >= 0 and temp < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp 
    return array


if __name__ == "__main__":
    l = InsertionSort(LIST)
    print(l)
