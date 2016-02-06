# Smallest positive number that is evenly divisible by all of the numbers from 1 to 20
# Oh boy is this slow. But it works!

counter = 20
running = True

def check_divisor(number):
    q = True
    for i in range(1, 21):
        if number % i != 0:
            q = False

    return q

while running:

    if not check_divisor(counter):
        counter += 20
    else:
        running = False

print(counter)



