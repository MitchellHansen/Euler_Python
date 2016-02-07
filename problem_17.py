#essentially an "english" number parser.
#count the letter counts of something like 399 "Three hundred and ninety nine"
#don't count spaces, hyphens

#                       one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve,
#                       thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
ones_word_count_dict = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12:6,
                        13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}

#                      ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
tens_word_count_dict = {1: 3, 2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}

hundred_letter_count = 7
and_letter_count = 3

def countLetters(number):
    letter_count = 0

    if number == 1000:
        return 11

    #count hundreds
    hundreds = int(number / 100)
    if hundreds > 0:
        letter_count += hundred_letter_count
        letter_count += ones_word_count_dict[hundreds]

    number -= hundreds * 100

    # if the number is a "teen"
    if number < 20 and number > 0:
        if hundreds > 0:
            letter_count += and_letter_count
        letter_count += ones_word_count_dict[number]
        return letter_count

    # if the number was an even 0
    elif number == 0:
        return letter_count

    # there is a tens and later a ones value
    else:
        if hundreds > 0:
            letter_count += and_letter_count

        tens = int(number / 10)
        letter_count += tens_word_count_dict[tens]

        number -= tens * 10
        if number != 0:
            letter_count += ones_word_count_dict[number]
        return letter_count


sum_letters = 0
for i in range(1, 1001):
    sum_letters += countLetters(i)

print(sum_letters)