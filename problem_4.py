import math


def isPalindrome(number):
    num_str = str(number)

    if len(num_str) % 2 != 0:
        return False

    for i in range(0, int(len(num_str) / 2)):
        if num_str[i] != num_str[len(num_str) - (i + 1)]:
            return False

    return True


largest_number = 0

for x in range(0, 999):
    for y in range(0, 999):
        if isPalindrome(x * y) and largest_number < x * y:
            largest_number = x * y

print(largest_number)