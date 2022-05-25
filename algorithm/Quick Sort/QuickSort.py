# coding=utf-8
"""
:Copyright: © 2022 Darren Liang, Inc. All Rights Reserved.

@Author: Darren Liang
@Date  : 2022-03-06
"""

LIST = [4, 2, 6, 5, 1, 3]

def swap(mylist, index1, index2):
    mylist[index1], mylist[index2] = mylist[index2], mylist[index1]

def pivot(mylist, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):

        if mylist[i] < mylist[pivot_index]:
            swap_index += 1
            swap(mylist, swap_index, i)
    swap(mylist, pivot_index, swap_index)
    return swap_index

def quicksort(mylist, left, right):
    if left < right:
        pivot_index = pivot(mylist, left, right)
        quicksort(mylist, left, pivot_index-1)
        quicksort(mylist, pivot_index+1, right)
    return mylist

def QuickSort(array):
    return quicksort(array, 0 , len(array)-1)

if __name__ == "__main__":
    # l = quicksort(LIST, 0,5 )
    l = QuickSort(LIST)
    print(l)

