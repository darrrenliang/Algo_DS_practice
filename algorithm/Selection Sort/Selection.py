# coding=utf-8
"""
:Copyright: © 2022 Darren Liang, Inc. All Rights Reserved.

@Author: Darren Liang
@Date  : 2022-03-05
"""

LIST = [4, 2, 6, 5, 1, 3]

def SelectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
        # array[i], array[min_index] = array[min_index], array[i]

    return array


if __name__ == "__main__":
    l = SelectionSort(LIST)
    print(l)
