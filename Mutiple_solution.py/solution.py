# Write a Python program access the index of a list
def index_list(list_item, index):
    # list_item is takes the value of of list
    # index takes in the value of the index
    list_item = list(list_item)
    index = int(index)

    return list_item[index]

print (index_list([1,2,3,4,5], 3))

#  Write a Python program to shuffle and print a specified list.
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

# Write a Python program to convert a list of characters into a string.
items  = ['Blue', 'Spoon', 'Chair', 'Fan']
for str_items in items:
    output = str(str_items)
    print (output)

# Write a Python program to select an item randomly from a list.
from random import choice
random_item = ['orange', 'rice', 'apple', 'pawpaw']
print ('Randomly picked',choice(random_item))