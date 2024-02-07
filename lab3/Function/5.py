def filter_prime(list):
    primeNumbers = [num for num in list if isprime(num)]
    return primeNumbers

def isprime(n):
    if n == 1:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
result = filter_prime(list)
print(result)  
'''
[2, 3, 5, 7, 11, 13]
'''
