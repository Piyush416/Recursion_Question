def getProduct(n): 
      
     
    if(n == 0): 
        return 1 
      
    
    return (n%10) * getProduct(n//10) ; 
  
 
print(getProduct(546)); 
  
