import math
# find the 10001st prime number

def isPrime(number):
    prime = True
    i = 2
    while i < math.sqrt(number) + 1:
        if number % i == 0:
            prime = False # found a factor, not prime
            break
        else:
            i += 1

    return prime

i = 1
primeCount = 1
while (primeCount != 10001):
    if isPrime(i):
        primeCount += 1
    i += 1

print(i)