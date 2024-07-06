def Mean(Arr, N): 
  
    if (N == 1): 
        return Arr[N - 1] 
    else: 
        return ((Mean(Arr, N - 1) *
                (N - 1) + Arr[N - 1]) / N) 
  


Arr = [33,54,87,55] 
N = len(Arr) 
print(Mean(Arr, N))