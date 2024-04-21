# Print all numbers from 1 to 100.
# If the number is divisible by 3, instead print 'Fizz'
# If the number is divisible by 5, instead print 'Buzz'
# If the number is divisible by both 3 and 5, print 'FizzBuzz'

for i in range(100):
    
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
