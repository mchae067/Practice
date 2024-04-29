import math

# Given an input of nickels, pennies, and a goal total, return True if the
# exact total can be made using the given nickels and pennies.
# Extra coins are ok.

# Count the total value of the highest value coins
# Apply to total, up until you need a smaller denomination of change
# Repeat for each coin of lower value if it can make the remaining total

def coins(nickels, pennies, goal_total):
    value_nickels = nickels * 5
    print(f"Value of nickels: {value_nickels}")
    num_pennies_required = goal_total % 5

    goal_total = goal_total - num_pennies_required - value_nickels
    print(f"Remaining goal total: {goal_total}")

    penny_goal = num_pennies_required - pennies

    return goal_total <= 0 and penny_goal <= 0


print(coins(2, 1, 10))
print(coins(2, 5, 12))
print(coins(2, 1, 12))
print(coins(200, 0, 12))


# Repeat the above, but with an input of a goal total, pennies, nickels, and dimes.

# Once again, but with an input of a goal total, pennies, nickels, dimes, and quarters.
