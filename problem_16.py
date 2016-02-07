import math

#print the sum of the digits of 2^1000

product = str('%f' % math.pow(2, 1000))
sum = 0

for char in product:
    if char == '.': # I can't really be bothered to do the conversion
        break
    sum += int(char)

print(product)
print(sum)