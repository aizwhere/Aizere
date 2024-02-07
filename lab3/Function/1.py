def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

number = int(input())
result = calculate_factorial(number)
print(result)
