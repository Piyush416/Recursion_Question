def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

num1 = 48
num2 = 18
gcd = gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {gcd}")