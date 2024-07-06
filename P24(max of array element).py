
def findMin(A, n): 
	if (n == 1): 
		return A[0] 
	return min(A[n - 1], findMin(A, n - 1)) 
 
A = [1, 4, 45, 6, 50, 10, 2] 
n = len(A) 
print(findMin(A, n)) 

