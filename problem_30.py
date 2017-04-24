

total_sum = 0

# just gonna take a wild guess and say there aren't any more higher than 1 million
for i in range(2, 1000000):
    num_str = str(i)
    sum = 0
    for ch in num_str:
        sum += pow(int(ch), 5)
    if sum == i:
        print(i)
        total_sum += i

print("Total sum {0}".format(total_sum))