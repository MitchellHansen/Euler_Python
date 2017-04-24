
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# top right
tr_sum = 1
for i in range(1, 501):
    tr_sum += pow(i * 2 + 1, 2)

# bottom right
br_sum = 1
br_tmp = 1
for i in range(1, 501):
    br_tmp += 2 + 8 * (i-1)
    br_sum += br_tmp

# bottom left
bl_sum = 1
for i in range(1, 501):
    bl_sum += pow(i * 2, 2) + 1

# top left
tl_sum = 1
tl_tmp = 1
for i in range(1, 501):
    tl_tmp += (i-1) * 8 + 6
    tl_sum += tl_tmp

# I guess the problem is looking to not repeat the center case to take away 3
print(tl_sum + bl_sum + br_sum + tr_sum - 3)