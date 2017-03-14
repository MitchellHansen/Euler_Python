import math

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def get_divisor_sum(input):

    divisor_sum = 0
    cutoff = math.ceil(input / 2)

    for idx, val in enumerate(range(cutoff), 1):
        if input % idx == 0:
            divisor_sum += idx

    return divisor_sum


def get_amicable():

    sums = []

    for i in range(10000):
        sums.append(get_divisor_sum(i))

    amicable_sum = 0

    for idx, val in enumerate(sums):
        if val < 10000:
            if sums[val] == idx and idx != val:
                amicable_sum += val + sums[val]
                print("VAL1_IDX: ", val)
                #print("VAL1_VAL: ", val)
                print("VAL2_VAL: ", sums[val])
                print("")

    return amicable_sum/2

print(get_amicable())

