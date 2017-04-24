import math

# n^2 + a*n + b , where |a|<1000 and |b|<1000


def is_prime(number):
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

largest_n = 0
largest_n_a = 0
largest_n_b = 0

for a in range(-1000, 1000):
    for b in range(-1000, 1000):

        n = 1
        while True:
            if not is_prime(abs(n*n + a*n + b)):
                break
            else:
                n += 1

        if n > largest_n:
            largest_n = n
            largest_n_a = a
            largest_n_b = b

    print("{0}, {1}".format(a, b))

print(largest_n)
print(largest_n_a)
print(largest_n_b)