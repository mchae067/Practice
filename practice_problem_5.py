from collections import deque

# Write a function that takes in a list as input and adds something (anything at all) to the end of the list,
# then return the new list

my_list = ["Dog", "Cat", "Mouse"]
my_list.append("Lizard")
print(my_list)

# Write a function that takes in a list as input and removes the third input
# then return the new list

my_list.pop(2)
print(my_list)

# Write a function that takes in a list as input and removes the second-to-last element
# then return the new list

my_list.append("Snake")
my_list.pop(-2)
print(my_list)

# Write a function that takes in two arguments, a set and a lookup value,
# return True if the lookup value is in the set, otherwise return False

my_set = my_list
print("Grape" in my_set)


# Write a function that takes in two lists of equal length, for example:
state_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut"]
capital_list = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford"]
# Return a Dictionary with the first list as the keys, and the second as the values

state_list = capital_list
print(state_list["Alabama"])
