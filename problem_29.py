import itertools

set_list = set()

permutation_list = list(itertools.product(range(2, 101), range(2, 101)))

for i in permutation_list:
    set_list.add(pow(i[0], i[1]))

print(len(set_list))


