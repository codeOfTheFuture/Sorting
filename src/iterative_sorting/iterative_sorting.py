# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        cur_val = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = cur_val

    return arr

print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = len(arr)
    while swap > 0:
        for i in range(0, len(arr)):
            n = i + 1
            if n <= len(arr) -1 and arr[i] > arr[n]:
                swap = len(arr)
                x = arr[i]
                arr[i] = arr[n]
                arr[n] = x
            else:
                swap -= 1
    return arr

print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr