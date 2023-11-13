number1 = int(input("Enter a number: "))
if number1 % 3 == 0 and number1 % 5 == 0:
    print('Tic Tac')
elif number1 % 3 == 0:
    print('Tic')
elif number1 % 5 == 0:
    print('Tac')

counter = 1
while counter <= 20:
    print(counter)
    counter += 1
counter = 1
while counter <= 20:
    if counter % 3 == 0 and counter % 5 == 0:
        print(counter, 'Tic Tac')
    elif counter % 3 == 0:
        print(counter, 'Tic')
    elif counter % 5 == 0:
        print(counter, 'Tac')
    counter += 1
counter += 1

import random
random.randint(1, 100)
random = int(input('Enter a random value: '))
attempts = 0
user_value: int = 0
while user_value <= 0 and attempts < 5:
    user_value = int(input('Enter a value greater than 0:'))
    attempts += 1
# count=0
# while(count<10):
#     print(count)
#     count=count+1


import random

print(random.randint(50, 100))

