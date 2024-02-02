a, b, c = int(input()), int(input()), int(input())
myList = [a, b, c]

def filter_prime(myList):
    prime_numbers = []
    for x in myList:
        if x != 1:
            for i in range(2, x):
                if x % i == 0:
                    break
            else:
                prime_numbers.append(x)
    return prime_numbers

answer = filter_prime(myList)
print(answer)
