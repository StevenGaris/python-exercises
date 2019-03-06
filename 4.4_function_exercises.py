

# Define a function named is_two.
# It should accept one input and return True if
# the passed input is either the number or the string 2,
# False otherwise.

# def is_two(input):
#     return input == 2 or input == '2' or input == 'two'
#
# print(is_two(2))
# print(is_two('2'))
# print(is_two('two'))
# print(is_two(4))


# Define a function named is_vowel.
# It should return True if the passed string is a vowel,
# False otherwise.

# def is_vowel(letter):
#     return letter in ['a', 'e', 'i', 'o', 'u']
#
# print(is_vowel('a'))
# print(is_vowel('e'))
# print(is_vowel('z'))
# print(is_vowel('b'))


# Define a function named is_consonant.
# It should return True if the passed string is a consonant, False otherwise.
# Use your is_vowel function to accomplish this.

# def is_consonant(letter):
#     return not is_vowel(letter)
#
# print(is_consonant('a'))
# print(is_consonant('e'))
# print(is_consonant('z'))
# print(is_consonant('b'))


# Define a function that accepts a string that is a word.
# The function should capitalize the first letter of the word if the word starts with a consonant.

# def upper_consonant(word):
#     if is_consonant(word[0]) == True:
#         return word.title()
#     else:
#         return word
#
# print(upper_consonant('alice'))
# print(upper_consonant('steven'))
# print(upper_consonant('ben'))
# print(upper_consonant('elizabeth'))


# Define a function named calculate_tip.
# It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# def calculate_tip(tip_percent, bill):
#     return (bill * tip_percent)
#
# print(calculate_tip(.16, 100))
# print(calculate_tip(.18, 100))
# print(calculate_tip(.2, 100))


# Define a function named apply_discount.
# It should accept an original price and a discount percentage,
# and return the price after the discount is applied.

# def apply_discount(original_price, discount_percentage):
#     return original_price - (original_price * discount_percentage)
#
# print(apply_discount(100, .50))
# print(apply_discount(100, .25))
# print(apply_discount(400, .75))
# print(apply_discount(100, -.50))



# Define a function named handle_commas
# It should accept a string that is a number that contains commas in it as input,
# and return a number as output.

# def handle_commas(number):
#     return int(number.replace(',',''))
#
# print(handle_commas('1,000'))
# print(handle_commas('1,000,000'))



# Define a function named get_letter_grade.
# It should accept a number and return the letter grade associated with that number (A-F).

# def get_letter_grade(grade):
#     if grade in range(88, 100):
#         return 'A'
#     elif grade in range(80, 87):
#         return 'B'
#     elif grade in range(67, 79):
#         return 'C'
#     elif grade in range(60, 66):
#         return 'D'
#     elif grade in range(0, 59):
#         return 'F'
#
# print(get_letter_grade(92))
# print(get_letter_grade(84))
# print(get_letter_grade(78))
# print(get_letter_grade(65))
# print(get_letter_grade(56))


# Define a function named remove_vowels
# that accepts a string and returns a string with all the vowels removed.

# def remove_vowels(word):
#     word = list(word)
#     no_vowel = []
#     for letter in word:
#         if letter not in ['a', 'e', 'i', 'o', 'u']:
#             no_vowel.append(letter)
#             no_vowel_str = ''.join(no_vowel)
#     return no_vowel_str
#
# print(remove_vowels('apple'))
# print(remove_vowels('saxophone'))
# print(remove_vowels('fun'))
# print(remove_vowels('car'))



# Define a function named normalize_name.
# It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores

# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed



def normalize_name(name):




# Write a function named cumsum
# that accepts a list of numbers
# and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]






# Bonus



# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.



# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.



# col_index('A') returns 1



# col_index('B') returns 2


# col_index('AA') returns 27