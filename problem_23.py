# A perfect number is a number for which the sum of its proper
# divisors is exactly equal to the number. For example, the sum
# of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors
# is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant
# numbers is 24. By mathematical analysis, it can be shown that all
# integers greater than 28123 can be written as the sum of two
# abundant numbers. However, this upper limit cannot be reduced any
# further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written
# as the sum of two abundant numbers.


# This program is essentially n^3 in the search and n^2 for the divisor count,
# so it runs reaalllyy slowly

import math
import pickle

def get_divisor_sum(input):

    divisor_sum = 0
    cutoff = math.ceil(input / 2)

    for idx, val in enumerate(range(cutoff), 1):
        if input % idx == 0:
            divisor_sum += idx

    return divisor_sum

def get_abundants():

    list = []

    for i in range(28123):
        sum = get_divisor_sum(i)
        if sum > i:
            list.append(i)

    with open('assets/outfile', 'wb') as fp:
        pickle.dump(list, fp)

    return list


# uncomment on any subsiquent runs to retrieve the cached data
# with open('assets/outfile', 'rb') as fp:
#     abundant_list = pickle.load(fp)

# comment this line out after the first run
abundant_list = get_abundants()
abundant_list.sort()

seen = {}
abundant_list = [seen.setdefault(x, x) for x in abundant_list if x not in seen]

summation = 0

for i in range(28123):

    found = False
    for first_number in abundant_list:

        if first_number > i:
            break

        search = i - first_number
        if search in abundant_list:
            found = True
            break

    if not found:
        summation += i



print(summation)
print(abundant_list)



