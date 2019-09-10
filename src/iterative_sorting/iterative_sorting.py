# TO-DO: Complete the selection_sort() function below

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # TO-DO: swap

    return arr


print(selection_sort(arr1))


arr1 = [5, 2, 3, 7, 0, 8]
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swapping = True
    while swapping:
        swapping = False
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapping = True

    return arr


print(bubble_sort(arr1))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
