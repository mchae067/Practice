# Display the fibonacci sequence up to 10 digits

# Given an input, display the fibonacci sequence up to n digits

do = 0
re = 1
print(do)
print(re)
for i in range(8):
    print(do + re)
    fa = do + re
    do = re
    re = fa