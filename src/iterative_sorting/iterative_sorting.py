# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for x in range(i, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x

        num = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = num

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = False
    isSorting = True
    index = 0

    while isSorting:
        if index >= len(arr) - 1:
            if not(swapped):
                return arr
            else:
                index = 0
                swapped = False

        if arr[index] > arr[index + 1]:
            num = arr[index]
            arr[index] = arr[index + 1]
            arr[index + 1] = num
            swapped = True

        index += 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
