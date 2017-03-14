
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

n_minus_1 = 1
n_minus_2 = 1
value = 0
index = 3

while True:

    value = n_minus_1 + n_minus_2
    if len(str(value)) == 1000:
        print(index)
        break

    n_minus_2 = n_minus_1
    n_minus_1 = value
    index += 1
