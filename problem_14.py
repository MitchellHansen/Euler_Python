#find the longest collatz sequence under one million
#if n is even n -> n/2
#if n is odd  n -> 3n + 1

longest_sequence = 0
matching_number = 0

for i in range(1, 1000001):
    sequence_count = 0
    number = i
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number *= 3
            number += 1
        sequence_count += 1

    if longest_sequence < sequence_count:
        longest_sequence = sequence_count
        matching_number = i

print(longest_sequence)
print(matching_number)