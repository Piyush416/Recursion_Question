def InsertionSort(array, i, j):
    n = len(array)
    if i < n:
        temp = array[i]
        j = i - 1
        if j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            InsertionSort(array, i, j - 1)
        array[j + 1] = temp
        InsertionSort(array, i + 1, j)
    return array

arr = [10, 8, 7, 50, 60, 3, 9, -1]
print(InsertionSort(arr, 1, 0))