def count_zeros(n):
    
    if n == 0:
        return 1
    
    if n < 10:
        return 0
    
    last_digit = n % 10
    
    rest_zeros = count_zeros(n // 10)
    
    if last_digit == 0:
        return rest_zeros + 1
    else:
        return rest_zeros

number = 10203040
print("Number of zeros in", number, ":", count_zeros(number))


