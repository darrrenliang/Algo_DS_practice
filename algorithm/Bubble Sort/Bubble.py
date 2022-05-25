# coding=utf-8
"""
:Copyright: © 2022 Darren Liang, Inc. All Rights Reserved.

@Author: Darren Liang
@Date  : 2022-03-05
"""

LIST = [4, 2, 6, 5, 1, 3]

def BubbleSort(array):
    for i in range(len(array), 0, -1):
        for j in range(i-1):
            if array[j] > array [j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


if __name__ == "__main__":
    l = BubbleSort(LIST)
    print(l)
