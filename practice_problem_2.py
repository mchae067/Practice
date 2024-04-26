# Given an input of nickels, pennies, and a goal total, return True if the
# exact total can be made using the given nickels and pennies.
# Extra coins are ok.

# def coins(nickels, pennies, goal_total):
#     for i in range(n+1):
#         if i % 5 == 0:
#             print("nickel")
#         elif i % 1 == 0:
#             print("penny")

nickels = 5
pennies = 1

def coins(nickels, pennies, goal_total):
    if nickels % goal_total and pennies % goal_total >= 0:
        return True
    else:
        return False

print(coins(2, 1, 10))
print(coins(2, 1, 12))

coins(2, 1, 10) # Should return True
coins(2, 1, 12) # Should return False

# Repeat the above, but with an input of a goal total, pennies, nickels, and dimes.

# Once again, but with an input of a goal total, pennies, nickels, dimes, and quarters.
