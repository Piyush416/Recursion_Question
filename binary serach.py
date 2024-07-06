def Algo(Arr, l, h, key):
    if l > h:
        return -1
    
    mid = l + (h - l) // 2
    
    if key == Arr[mid]:
        return mid
    elif key < Arr[mid]:
        return Algo(Arr, l, mid - 1, key)
    else:
        return Algo(Arr, mid + 1, h, key)

Arr = [1, 2, 3, 5, 45, 55, 667, 8]
print(Algo(Arr, 0, len(Arr) - 1, 55))
