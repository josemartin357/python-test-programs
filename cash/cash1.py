from cs50 import get_float

# do while loop to request input and check if it’s equal/over than 1
while True:
    # asking user input 
    dollars = get_float("Amount owed: ")
    #checking if input equal or higher than 1
    if dollars >= 0:
        # if condition met, exit loop
        break

# need value in get_float to represent an integer to deduct 25, 10, 5 and 1
cents = round(dollars * 100)

# set initial counter as 0
coins = 0

# using do while loops to check if from coins, 25 or 10 or 5 or 1 can be deducted 
# 25 cents
while cents >= 25:
        cents -= 25
        coins += 1


# 10 cents
while cents >= 10:
        cents -= 10
        coins += 1

# 5 cents
while cents >= 5:
        cents -= 5
        coins += 1

# 1 cent
while cents >= 1:
        cents -= 1
        coins += 1


# print counter 
print(coins)