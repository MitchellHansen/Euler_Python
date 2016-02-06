import math
#find the first triangle number with over five hundred divisors


def countDivisors(number):
    count = 0
    for i in range (1, int(math.sqrt(number))):
        if number % i == 0:
            count += 1
    return count

running = True
counter = 1
while(running):
    sum = 0
    for i in range(0, counter + 1):
        sum += i
    if countDivisors(sum) > 400:
        print(counter)
        running = False
    counter += 1

print(counter)
