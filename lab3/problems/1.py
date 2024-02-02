def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)
    
n = int(input())

answer = calculate_factorial(n)
print(answer)