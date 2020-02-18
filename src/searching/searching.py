# STRETCH: implement Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    start = 0
    end = len(arr) - 1

    # TO-DO: add missing code
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, start, end):

    middle = (start + end) // 2

    if len(arr) == 0:
        return -1  # array empty

    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        end = middle - 1
        return binary_search_recursive(arr, target, start, end)
    else:
        start = middle + 1
        return binary_search_recursive(arr, target, start, end)
