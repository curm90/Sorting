# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arrA_index = 0
    arrB_index = 0

    for i in range(elements):
        if len(arrA) <= arrA_index:
            merged_arr[i] = arrB[arrB_index]
            arrB_index += 1
        elif len(arrB) <= arrB_index:
            merged_arr[i] = arrA[arrA_index]
            arrA_index += 1
        elif arrB[arrB_index] < arrA[arrA_index]:
            merged_arr[i] = arrB[arrB_index]
            arrB_index += 1
        else:
            merged_arr[i] = arrA[arrA_index]
            arrA_index += 1

    return merged_arr


list1 = [5, 77, 3, 1, 99, 32, 12, 56, 2, 19]

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left_arr = arr[:middle]
        right_arr = arr[middle:]

        return merge(merge_sort(left_arr), merge_sort(right_arr))


print(merge_sort(list1))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
