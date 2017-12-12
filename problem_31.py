
# thank you http://algorithms.tutorialhorizon.com/dynamic-programming-coin-change-problem/

coin_list = [1, 2, 5, 10, 20, 50, 100, 200]


def coin(v, amount):

    solution = [[0 for x in range(amount + 1)] for y in range(len(v) + 1)]

    if amount == 0:
        return 0

    for i in range(0, len(v) + 1):
        solution[i][0] = 1

    for i in range (1, amount + 1):
        solution[0][i] = 0

    for i in range(1, len(v) + 1):
        for j in range(1, amount + 1):
            if v[i - 1] <= j:
                solution[i][j] = solution[i - 1][j] + solution[i][j - v[i - 1]]
            else:
                solution[i][j] = solution[i - 1][j]
    return solution[len(v)][amount]


print(coin(coin_list, 200))