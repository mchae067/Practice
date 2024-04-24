# Display the fibonacci sequence up to 10 digits
do = 0
re = 1
print(do)
print(re)
for i in range(8):
    print(do + re)
    fa = do + re
    do = re
    re = fa


# Given an input, display the fibonacci sequence up to n digits
def fibonacci(n):
    n_minus_2 = 0
    n_minus_1 = 1
    if n == 0:
        print("Nothing! You get nothing!")
    elif n == 1:
        print(n_minus_2)
    elif n == 2:
        print(n_minus_2)
        print(n_minus_1)
    else:
        print(n_minus_2)
        print(n_minus_1)
        for i in range(n-2):
            print(n_minus_2 + n_minus_1)
            sum = n_minus_2 + n_minus_1
            n_minus_2 = n_minus_1
            n_minus_1 = sum


fibonacci(10)
fibonacci(0)
fibonacci(1)
fibonacci(2)
