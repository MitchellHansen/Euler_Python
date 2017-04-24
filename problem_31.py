
# solving this recursively is an interesting solution

import itertools

set_list = set()
permutation_list = list(itertools.combinations(list([1, 2, 5, 10, 20, 50, 100, 200]), 2))

success_count = 0


def recursive_coin_add(value, ciel):

    if value == ciel:
        global success_count
        success_count += 1
        return

    if 1 + value <= ciel:
        recursive_coin_add(1 + value, ciel)

    if 2 + value <= ciel:
        recursive_coin_add(2 + value, ciel)

    if 5 + value <= ciel:
        recursive_coin_add(5 + value, ciel)

    if 10 + value <= ciel:
        recursive_coin_add(10 + value, ciel)

    if 20 + value <= ciel:
        recursive_coin_add(20 + value, ciel)

    if 50 + value <= ciel:
        recursive_coin_add(50 + value, ciel)

    if 100 + value <= ciel:
        recursive_coin_add(100 + value, ciel)

    if 200 + value <= ciel:
        recursive_coin_add(200 + value, ciel)

recursive_coin_add(0, 200)

print(success_count)