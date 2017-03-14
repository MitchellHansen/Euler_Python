
prev_two = 1
prev_one = 0
fib_num = 0
sum = 0

while True:
    if fib_num > 4000000:
        break

    fib_num = prev_one + prev_two

    if fib_num % 2 == 0:
        sum += fib_num

    prev_two = prev_one
    prev_one = fib_num

print(sum)
