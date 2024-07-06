def binary(n):
    if n == 0:
        return ""
    
    quotient = n // 2
    remainder = n % 2
    
    binary_representation = binary(quotient)
    
    return binary_representation + str(remainder)

decimal_number = 27
print("Binary representation of", decimal_number, ":", binary(decimal_number))
