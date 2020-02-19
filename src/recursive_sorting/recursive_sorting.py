# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    arrAi = 0
    arrBi = 0
    index = 0

    print(f'Elements: {elements}')
    print(f'merged_arr: {merged_arr}')
    print(f'arrAi: {arrAi}')
    print(f'arrBi: {arrBi}')
    print(f'index: {index}')
    while arrAi < len(arrA) and arrBi < len(arrB):
        if arrB[arrBi] > arrA[arrAi]:
            merged_arr[index] = arrA[arrAi]
            print(f'merged_arr[index]: {merged_arr[index]}')
            arrAi += 1
            index += 1
        else:
            merged_arr[index] = arrB[arrBi]
            print(f'merged_arr[index]: {merged_arr[index]}')

            arrBi += 1
            index += 1

    while(arrAi < len(arrA)):
        merged_arr[index] = arrA[arrAi]
        print(f'merged_arr[index]: {merged_arr[index]}')

        arrAi += 1
        index += 1

    while(arrBi < len(arrB)):
        merged_arr[index] = arrB[arrBi]
        print(f'merged_arr[index]: {merged_arr[index]}')
    
        arrBi += 1
        index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = arr[:middle]
        right = arr[middle:]
        arrA = merge_sort(left)
        arrB = merge_sort(right)
        return merge(arrA, arrB)

my_arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(merge_sort(my_arr))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
