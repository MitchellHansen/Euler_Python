import math

highest_factor = 1

for x in range(3, int(math.sqrt(600851475143)), 2):
    if 600851475143 % x == 0:

        prime = True
        i = 3
        while i * i < x:
            if x % i == 0:
                prime = False # found a factor, not prime
                break
            else:
                i += 2

        if prime:
            highest_factor = x

print(highest_factor)