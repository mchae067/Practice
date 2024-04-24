# Given an input of nickels, pennies and a goal total, return True if the
# exact total can be made using the given nickels and pennies.
# Extra coins are ok.



def Coin(n):
    for i in range(n+1):
        if i % 5 == 0:
            print("nickel")
        elif i % 1 == 0:
            print("penny")

Coin(10)

# Repeat the above, but with an input of a goal total, pennies, nickels, and dimes.

# Once again, but with an input of a goal total, pennies, nickels, dimes, and quarters.
