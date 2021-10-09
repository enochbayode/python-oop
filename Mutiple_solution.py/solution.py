# # Write a Python program access the index of a list
# def index_list(list_item, index):
#     # list_item is takes the value of of list
#     # index takes in the value of the index
#     list_item = list(list_item)
#     index = int(index)

#     return list_item[index]

# print (index_list([1,2,3,4,5], 3))

# #  Write a Python program to shuffle and print a specified list.
# from random import shuffle
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(color)
# print(color)

# # Write a Python program to convert a list of characters into a string.
# items  = ['Blue', 'Spoon', 'Chair', 'Fan']
# for str_items in items:
#     output = str(str_items)
#     print (output)

# # Write a Python program to select an item randomly from a list.
# from random import choice
# random_item = ['orange', 'rice', 'apple', 'pawpaw']
# print ('Randomly picked',choice(random_item))

# # Write a Python program to remove all elements from a given list present in another list.
# list1 = [1,2,3,4,5,6,7,8]
# list2 = [2,4,6,8]

# for n in list2:
#     if n in list1:
#         list1.remove(n)
# print (list1)

# # list1 = [list1.remove(n) for n in list2[if n in list1]]

# #  Write a Python program to reverse strings in a given list of string values.
# items = ['blue', 'red', 'green', 'yellow']
# for i in items:
#     result = i[::-1]
#     print (result)

# Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers.
Original_list = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
max_num = max(Original_list)
min_num = min(Original_list)
print ('The index position of the maximum value: ', Original_list.index(max_num))
print ('The index position of the minimum value: ', Original_list.index(min_num))