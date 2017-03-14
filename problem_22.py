import ast

# read in the file, convert to a list
f = open('assets/problem_21_names.txt', 'r')  # We need to re-open the file
data = ast.literal_eval(f.read())
f.close()

data.sort()

sum = 0

for idx, name in enumerate(data):

    word_sum = 0
    for letter in name:
        word_sum += ord(letter) - 65 + 1

    sum += word_sum * (idx+1)

print(sum)