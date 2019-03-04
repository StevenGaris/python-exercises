
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

# Write some code that prompts the user for a number,
# then shows a multiplication table up through 10 for that number.

user_number = int(input('Pick a number: '))

for user_number






# The input function can be used to prompt for input and use that input in your python code.
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number.
# (Hints: first make sure that the value the user entered is a valid number, also
# note that the input function returns a string, so you'll need to convert this to a numeric type.)

# user_number = int(input("Pick a positive number: "))
# if user_number < 1:
#     print("Your number was not a positive number, try again.")
# else:
#     for n in range(0, user_number + 1):
#         print(n)


# Write a program that prompts the user for a positive integer.
# Next write a loop that prints out the numbers from the number the user entered down to 1.

# user_number = int(input("Pick a positive number: "))
# if user_number < 1:
#     print("Your number was not a positive number, try again.")
# else:
#     for n in range(0, user_number):
#         print(user_number - n)

