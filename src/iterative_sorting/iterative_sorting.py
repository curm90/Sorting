# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    pass
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    pass
    return arr


list1 = [7, 5, 2, 1, 9, 12, 34, 22, 3]

print(selection_sort(list1))
