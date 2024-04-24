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

# tuples are immutable, and are useful for unpacking
my_tuple = "apple", "orange", "pear"
fruit1, fruit2, fruit3 = my_tuple
print(fruit1, fruit2, fruit3)


# Stacks, Queues, Heap
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
my_dictionary = {"Illinois": "Springfield", "Delaware": "Dover", "Alaska": "Rejkasjdfkdjs"}
print(my_dictionary["Alaska"])


# Functions
def my_func(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

my_func("Diego", "Diecinueve")

def add_one(number):
    print(number+1)

add_one(10)
