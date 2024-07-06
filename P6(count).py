def count(n):
     print(n)
     if n == 0:
         return             
     else:
         count(n - 1)   
print(count(5))         