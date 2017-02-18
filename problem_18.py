grid = [
    [75],
    [95,64],
    [17,47,82],
    [18,35,87,10],
    [20, 4,82,47,65],
    [19, 1,23,75, 3,34],
    [88, 2,77,73, 7,63,67],
    [99,65, 4,28, 6,16,70,92],
    [41,41,26,56,83,40,80,70,33],
    [41,48,72,33,47,32,37,16,94,29],
    [53,71,44,65,25,43,91,52,97,51,14],
    [70,11,33,28,77,73,17,78,39,68,17,57],
    [91,71,52,38,17,14,91,43,58,50,27,29,48],
    [63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
    [ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23]]

highest_sum = 0

# take the current number index at grid slice
# call into the index, and then the index + 1 on the next grid slice

def recursive_solver(index, level):

    if level == len(grid)-1:
        return grid[level][index]

    else:
        val1 = recursive_solver(index, level + 1) + grid[level][index]
        val2 = recursive_solver(index + 1, level + 1) + grid[level][index]

        if val1 > val2:
            return val1
        else:
            return val2



print(recursive_solver(0, 0))