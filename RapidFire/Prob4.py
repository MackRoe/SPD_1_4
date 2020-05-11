# Given two sorted arrays, merge them into a single sorted array.
''' concatonate the arrays, then sort the concatonated array

define the function to accept two arguments, being the two arrays.
create a new list to store the merged array
then concatonate the two arrays together and sort the resulting array
'''


def merge_and_sort(ls1, ls2):
    merged_array = ls1 + ls2
    print('merged array: ', merged_array)
    merged_array.sort()
    return merged_array


Array1 = [1, 2, 3]
Array2 = [5, 6, 7]

# expected output [1, 2, 3, 5, 6, 7]

print(merge_and_sort(Array2, Array1))
