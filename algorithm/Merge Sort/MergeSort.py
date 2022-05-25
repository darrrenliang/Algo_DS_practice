# coding=utf-8
"""
:Copyright: © 2022 Darren Liang, Inc. All Rights Reserved.

@Author: Darren Liang
@Date  : 2022-03-06
"""

LIST = [4, 2, 6, 5, 1, 8, 7, 3]

def MergeSort(array):
    # List with length less than is already sorted
    if len(array) == 1:
        return array

    # To ensure all partitions are broken down into their individual components,
    # the merge_sort function is called and a partitioned portion of the list is passed as a parameter
    middle = int(len(array)/2)
    left   = array[:middle]
    right  = array[middle:]

    # The merge_sort function returns a list composed of a sorted left and right partition.  
    return merge(MergeSort(left), MergeSort(right))


def merge(left, right):
    # Initialize an empty list output that will be populated with sorted elements.
    # Initialize two variables i and j which are used pointers when iterating through the lists.
    output = []
    i = j = 0

    # Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # Compare the elements at every position of both lists during each iteration
        if left[i] < right[j]:
            # output is populated with the lesser value
            output.append(left[i])
            # Move pointer to the right
            i += 1
        else:
            output.append(right[j])
            j += 1
    # The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    print(left[i:], right[j:], output)        
    return output

if __name__ == "__main__":
    sort = MergeSort(LIST)
    print(sort)
    pass