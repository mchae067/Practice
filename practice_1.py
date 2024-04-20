#!/usr/bin/env python3

# Welcome to Python! Python is a scripting language, meaning it is interpreted at runtime.
# Java > fed into compiler > spits out binaries
# Python > interpreter reads code at runtime

print("Hello World")


# int
one = 1
two = 2
one_hundred = 100
two_hundred = 200

foo = 5
# bar is 6
bar = foo + 1
# bar is 7
bar = 7
purple = 1000

print(f"Printing literal values of 1 + 2: {1+2}")
print(f"Printing literal values of one + two: {one+two}")
print(f"Printing literal values of foo + purple: {foo + purple}")


# float
foo_float = 1.5
bar_float = 3.0


# long
long_number = 100000000000000000000000000


# boolean
foo_bool = True
bar_bool = False
# Reassigning this for the purposes of teaching, don't do this in actual code
purple = 1000
# condition is True
condition = (purple == 1000)
print(condition)

if foo_bool:
    print("Random phrase!")
if bar_bool:
    print("A different random phrase!")
if purple == 1000:
    print("Condition passed!")
if purple > 1000:
    print("Purple is greater than 1000!")
if purple - 100 <= 1000:
    print("Purple minus 100 is less than or equal to 1000!")

# Purple has not been reassigned in memory at all, therefore, the value stays at 1000
print(purple)


# string
# Strings are arrays of chars
character = 'a'
output_value = "Hello World!"
output_value2 = " How are you doing?"

print(output_value)

message = output_value + output_value2
print(message)
print(message[1])
# Split separates a string into an array of smaller strings, separated by an input index
split_message = message.split(" ")
print(split_message)
