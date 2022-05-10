from cs50 import get_float

# do while loop to request input and check if it’s equal/over than 1
while True:
    # asking user input 
    amount_owed = get_float("Amount owed: ")
    # checking if input equal or higher than 1
    if amount_owed >= 0:
        # if condition met, exit loop
        break

# need value in get_float to represent an integer to deduct 25, 10, 5 and 1
coins = round(amount_owed * 100)

# set initial counter as 0
counter = 0

# in an array, we add the quarter, dime, nickel and penny values
values = [25, 10, 5, 1]

# using a loop that runs thru array using remainder and divider operations to iterate and give coins and counter new values
for value in values:
    # in every loop, counter takes the value of the division of coins by values in array. Example: 41 // 25 = 1, so counter = 1. In next line coins takes a new value. counter = 1 + (16 // 10) so counter = 1 + 1 …. And so on
    counter = counter + coins // value
    # in every loop, coins takes the value of itself remainder of values of array. For example: coins = 41 % 25, so coins = 16 .. and so on 
    coins = coins % value

# print counter 
print(counter)