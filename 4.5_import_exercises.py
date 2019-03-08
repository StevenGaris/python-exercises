

# import the module and refer to the function with the . syntax

# import functions_exercises
# print(functions_exercises.is_two(3))


# use from to import the function directly

# from functions_exercises import is_two
# print(is_two(3))


# use from and give the function a different name

# from functions_exercises import is_two as check_two
# print(check_two(3))


# For the following exercises,
# read about and use the itertools module from the standard library
# to help you solve the problem.

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# from itertools import product
#
# print(len(list(product('abc','123'))))
# print(list(product('abc','123')))



# How many different ways can you combine two of the letters from "abcd"?

# from itertools import permutations
#
# print(len(list(permutations('abcd', 2))))
# print(list(permutations('abcd', 2)))





from json import load

file = open('profiles.json', 'r')

file_data = load(file)

# Total number of users

list_of_ids = []

for element in file_data:
    list_of_ids.append(element['_id'])

total_users = len(list_of_ids)

# print(total_users)



# Number of active users

active_list = []

for element in file_data:
    if element['isActive'] == True:
        active_list.append(element['isActive'])

active_user_count = len(active_list)

# print(active_user_count)


# Number of inactive users


inactive_count = len(list_of_ids) - len(active_list)
#
# print(inactive_count)


# Grand total of balances for all users

total_list = []

for element in file_data:
    total_list.append(float(element['balance'].replace('$','').replace(',','')))

grand_total = sum(total_list)

# print(grand_total)



# Average balance per user

avg_bal = grand_total / total_users

# print(avg_bal)


# User with the lowest balance

name_list = []
bal_list = []

for element in file_data:
    name_list.append(element['name'])
    bal_list.append(float(element['balance'].replace('$','').replace(',','')))

min_bal = min(bal_list)
min_index = bal_list.index(min_bal)
min_name = name_list[int(min_index)]

# print(min_name)




# User with the highest balance

name_list = []
bal_list = []

for element in file_data:
    name_list.append(element['name'])
    bal_list.append(float(element['balance'].replace('$','').replace(',','')))

max_bal = max(bal_list)
max_index = bal_list.index(max_bal)
max_name = name_list[int(max_index)]

# print(max_name)



# Most common favorite fruit

fruit_list = []

for element in file_data:
    fruit_list.append(element['favoriteFruit'])

# print(max(fruit_list))



# Least most common favorite fruit

fruit_list = []

for element in file_data:
    fruit_list.append(element['favoriteFruit'])

# print(min(fruit_list))


# Total number of unread messages for all users

greeting_list = []

for element in file_data:
    greeting_list.append(element['greeting'])





print(greeting_list)
