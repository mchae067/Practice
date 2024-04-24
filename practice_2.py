from collections import deque


# Data Structures

# Lists, Tuples, Sets
# The building blocks of other Python data structures

# List Documentation: https://docs.python.org/3/tutorial/datastructures.html
my_list = []
my_list.append("apple")
my_list.append("orange")
print(f"Current list: {my_list}")

my_other_list = [i for i in range(20)]
print(my_other_list)

del my_list[0]
print(my_list)

# A set is an unordered collection with no duplicate elements
my_set = {"apple", "orange", "pear"}
print(my_set)
# Checking to see if grape is in the set, return True if so, False otherwise
print("grape" in my_set)
# Adding or deleting from a set requires a lookup of a specific value
my_set.remove("pear")
my_set.add("banana")
print(my_set)
# You can instantiate a set like this. Since there can't be duplicate elements,
# only a, b, r, c, and d will be added
a = set('abracadabra')
print(a)

# tuples are immutable, and are useful for unpacking
my_tuple = "apple", "orange", "pear"
fruit1, fruit2, fruit3 = my_tuple
print(fruit1, fruit2, fruit3)


# Stacks, Queues
my_stack = ["apple", "orange", "pear"]
my_stack.append("grape")
my_stack.append("pineapple")
my_stack.pop()
print(my_stack)

my_queue = deque(["apple", "orange", "pear"])
my_queue.append("grape")
my_queue.popleft()
print(my_queue)


# Dictionaries
my_dictionary = {"apple": "red fruit, tastes sweet", "orange": "orange citrus, tastes sour", "carrot": "a  carrot"}
print(my_dictionary["carrot"])
state_capitals = {"Illinois": "Springfield", "Delaware": "Dover", "Alaska": "Juneau"}
print(state_capitals["Alaska"])
# You can add entries to a dictionary like so:
state_capitals["Virginia"] = "Richmond"
# And remove like so:
del state_capitals["Alaska"]
print(state_capitals)


# Functions
def my_func(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

my_func("Diego", "Diecinueve")

def add_one(number):
    print(number+1)

add_one(10)

# If you want your function to output something, use a 'return' statement
def add_one_with_output(number):
    return number+1

# This will print 21
print(add_one_with_output(20))

def even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

print(even_or_odd(2))
print(even_or_odd(5))

# You can also assign the value of a function with a return to a variable

func_output_string = even_or_odd(4)
print(func_output_string)
