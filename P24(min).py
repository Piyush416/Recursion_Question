def findMin(Arr, n): 
	if (n == 1): 
		return Arr[0] 
	return min(Arr[n - 1], findMin(Arr, n - 1)) 
 
Arr = [1, 4, 45, 6, 50, 10, 2] 
n = len(Arr) 
print(findMin(Arr, n)) 
