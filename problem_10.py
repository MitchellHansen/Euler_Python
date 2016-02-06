import math

#find the sum of all primes under 2 million
#once again, it works, but it's sloooowwwww

def isPrime(number):
    if number == 1:
        return False
    prime = True
    i = 2
    while i < math.sqrt(number) + 1:
        if number % i == 0:
            prime = False # found a factor, not prime
            break
        else:
            i += 1

    return prime

number = 3
sum = 2

while (number < 2000000):
    if isPrime(number):
        sum += number
    number += 2

print(number)
print(sum)