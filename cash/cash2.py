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

# using a loop that runs thru array and checks if from coins 25 or 10 or 5 or 1 can be deducted
for value in values:
    while coins >= value:
        coins -= value
        counter += 1

# print counter 
print(counter)