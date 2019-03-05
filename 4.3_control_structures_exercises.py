
# Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not

# day_of_the_week = input('What day of the week is it? ')
# if day_of_the_week == 'Monday':
#     print('It is Monday')
# else:
#     print('It is not Monday.')


# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# day_of_the_week = input('What day of the week is it? ')
# if day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
#     print("It's the weekend!")
# else:
#     print("It's a weekday.")


# create variables and make up values for

# the number of hours worked in one week
# hours_worked_this_week = 41

# the hourly rate
# hourly_rate = 19

# how much the week's paycheck will be
# paycheck_amount_this_week = hours_worked_this_week * hourly_rate

# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# if hours_worked_this_week > 40:
#     over_time_hours = hours_worked_this_week - 40
#     over_time_pay_rate = hourly_rate * 1.5
#     over_time_pay = over_time_hours * over_time_pay_rate
#     regular_rate = 40 * hourly_rate
#     total_pay = regular_rate + over_time_pay
#     print('You made $' + str(total_pay) + ' this week.')
# else:
#     print('You made $' + str(paycheck_amount_this_week) + ' this week.')



# Loop Basics

# While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

# i = 5
# while i <= 15:
#     print(i)
#     i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

# i = 0
# while i < 101:
#     print(i)
#     i += 2

# Alter your loop to count backwards by 5's from 100 to -10.

# i = 100
# while i >= -10:
#     print(i)
#     i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line
# while the number is less than 1,000,000. Output should equal:

# i = 2
# while i < 1000000:
#     print(i)
#     i *= i

# i = 100
# while i >= 5:
#     print(i)
#     i -= 5


# For Loops

# I
# Write some code that prompts the user for a number,
# then shows a multiplication table up through 10 for that number.

# user_number = int(input('Pick a number: '))
# for num in range(1,11):
#     print(user_number, ' x ', num, ' = ', (user_number * num))

# II
# num = 1
# for n in range(1,10):
#     print(str(n) * n)
#     n += 1



# break and continue

# I
# Prompt the user for an odd number between 1 and 50.
# Use a loop and a break statement to continue prompting the user if they enter invalid input.
# (Hint: use the isdigit method on strings to determine this).
# Use a loop and the continue statement to output all the odd numbers between 1 and 50,
# except for the number the user entered.

# user_number = input('Pick an odd number between 1 and 50: ')
# while not user_number.isdigit() or int(user_number) % 2 == 0 or int(user_number) > 50:
#     user_number = input('Pick an odd number between 1 and 50: ')
#     continue
# user_number = int(user_number)
# print('The number to skip is:', user_number)
# print('')
# for num in range(1,51):
#     if num % 2 == 1 and num != user_number:
#         print('Here is an odd number:', num)
#     if num == user_number:
#         print('Yikes! Skipping number:', user_number)


# The input function can be used to prompt for input and use that input in your python code.
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number.
# (Hints: first make sure that the value the user entered is a valid number,
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# user_number = input("Pick a positive number: ")
# while not user_number.isdigit() or int(user_number) < 1:
#     user_number = input("Pick a positive number: ")
#     continue
# user_number = int(user_number)
# if user_number < 1:
#     print("Your number was not a positive number, try again.")
# else:
#     for n in range(0, user_number + 1):
#         print(n)


# Write a program that prompts the user for a positive integer.
# Next write a loop that prints out the numbers from the number the user entered down to 1.

# user_number = input("Pick a positive number: ")
# while not user_number.isdigit() or int(user_number) < 1:
#     user_number = input("Pick a positive number: ")
#     continue
# user_number = int(user_number)
# if user_number < 1:
#     print("Your number was not a positive number, try again.")
# else:
#     for n in range(0, user_number):
#         print(user_number - n)


# Fizzbuzz

# numbers = range(1,101)
# for num in numbers:
#     if num % 3 == 0 and num % 5 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)

# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

# user_number = int(input('What number would you like to go up to? '))
# print('Here is your table.')
# for num in range(1, user_number + 1):
#     print("{:3d}".format(num), "{:3d}".format(num ** 2), "{:3d}".format(num ** 3))
#
# answer = (input('Would you like to continue? '))
# if answer == 'no':
#     print('End Process')
#
# while answer == 'yes':
#     user_number = int(input('What number would you like to go up to? '))
#     print('Here is your table.')
#
#     for num in range(1, user_number + 1):
#         print("{:3d}".format(num), "{:3d}".format(num ** 2), "{:3d}".format(num ** 3))
#
#     answer = (input('Would you like to continue? '))
#
#     if answer == 'no':
#         print('End Process')


# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.

# user_score = int(input('Pick a number grade from 0 to 100: '))
# if user_score in range(88,100):
#     print(user_score, ' is an A.')
# elif user_score in range(80,87):
#     print(user_score, ' is a B.')
# elif user_score in range(67,79):
#     print(user_score, ' is a C.')
# elif user_score in range(60,66):
#     print(user_score, ' is a D.')
# elif user_score in range(0,59):
#     print(user_score, ' is a F.')
#
# user_answer = input('Would you like to get another grade? ')
#
# if user_answer == 'no':
#     print('End Process')
#
# while user_answer == 'yes':
#     user_score = int(input('Pick a number grade from 0 to 100: '))
#     if user_score in range(88, 100):
#         print(user_score, ' is an A.')
#     elif user_score in range(80, 87):
#         print(user_score, ' is a B.')
#     elif user_score in range(67, 79):
#         print(user_score, ' is a C.')
#     elif user_score in range(60, 66):
#         print(user_score, ' is a D.')
#     elif user_score in range(0, 59):
#         print(user_score, ' is a F.')
#
#     user_answer = (input('Would you like to get another grade? '))
#
#     if user_answer == 'no':
#         print('End Process')


# Create a list of dictionaries where each dictionary represents a book that you have read.
# Each dictionary in the list should have the keys title, author, and genre.
# Loop through the list and print out information about each book.

# books = ({'name': 'Harry Potter', 'author': 'JK Rowling', 'genre': 'Fantasy'},
#          {'name': 'Eragon', 'author': 'Christopher Paolini', 'genre': 'Fantasy'},
#          {'name': 'Lord of the Rings', 'author': 'JRR Tolkien', 'genre': 'Fantasy'})
#
# for element in books:
#     print(element['name'])



# Prompt the user to enter a genre, then loop through your books list and
# print out the titles of all the books in that genre.

books = ({'name': 'Harry Potter', 'author': 'JK Rowling', 'genre': 'Fantasy'},
         {'name': 'Eragon', 'author': 'Christopher Paolini', 'genre': 'Fantasy'},
         {'name': 'Lord of the Rings', 'author': 'JRR Tolkien', 'genre': 'Fantasy'},
         {'name': 'Enders Game', 'author': 'Orson Scott Card', 'genre': 'Scifi'},
         {'name': 'The Shining', 'author': 'Stephen King', 'genre': 'Horror'},
         {'name': 'It', 'author': 'Stephen King', 'genre': 'Horror'},)

user_pick = input('Pick a genre: ')

for element in books:
    if element['genre'] == user_pick:
        print(element['name'])


