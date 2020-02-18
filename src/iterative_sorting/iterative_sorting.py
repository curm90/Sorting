# Selection Sort
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # Swap elements
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# Bubble sort
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap elements
                swapped = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    pass
    return arr
