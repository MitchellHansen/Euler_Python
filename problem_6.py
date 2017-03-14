#Difference between the sum of squares and the square of the sum of the first 100 numbers

#find the sum of the squares
sum_of_squares = 0
for i in range (1, 101):
    sum_of_squares += i * i

#find the square of the sum
square_of_sums = 0
for i in range(1, 101):
    square_of_sums += i

square_of_sums *= square_of_sums

#find the difference
square_of_sums -= sum_of_squares
print(square_of_sums)