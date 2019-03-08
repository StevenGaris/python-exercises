


# Read the contents of your last exercise file into a variable.
#
# Print out every line in the file


# with open('import_exercises.py') as f:
#     lines = f.read()
#
# print(lines)



# Print out every line in the file, but add a line numbers

with open('import_exercises.py') as f:
    lines = f.readlines()

line_num = []

for line in lines:
    line_num.append('3' + line)

print(line_num)




# Write some python code to create a grocery list.

# Create a variable named grocery_list.
# It should be a list, and the elements in the list should be
# a least 3 things that you need to buy from the grocery store.



# Create a function named make_grocery_list.
# When run, this function should write the contents of the grocery_list variable
# to a file named my_grocery_list.txt.



# Create a function named show_grocery_list.
# When run, it should show each item on the grocery list.



# Create a function named buy_item.
# It should accept the name of an item on the grocery list,
# and remove that item from the list.
#


