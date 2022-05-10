# write a program that prompts the user for a credit card number and then reports (via print) whether it is a valid American Express, MasterCard, or Visa card number.
from cs50 import get_int

def main():
    # Using a method similar to while loop to request user number and check if number entered is over 0
    while True:
        # First we ask card number
        card_number = get_int("Enter card number: ")
        # if number entered higher than 0 ...
        if card_number > 0:
            # ... we exit loop
            break

    # if running card_number on check_validity function works ...
    if check_validity(card_number):
        # ... then we call function card_bank on card_number
        card_bank(card_number)
    # otherwise, we inform user card_number is invalid
    else:
        print("INVALID CARD")

# function takes argument, checks validity and returns true or false
def check_validity(number):
    # set initial value of sum
    sum = 0
    # converting number into a string, then reversing it
    reversed_string = reversed(str(number))
    # using enumerate() to target count and value from an iterable. i is the count, c is the value
    for i, c in enumerate(reversed_string):
        # if the i string divisible by 2, 
        if i % 2 == 0:
            # when during the loop i is even, sum takes value of the original odd values that dont have to be * 2
            # 456789 // 9 [8] 7 [6] 5 [4] // here sum adds value of 9, and then 7 and then 5
            sum = sum + int(c) 
        else:
            # when during loop, i string is even, define variable that will * 2
            # 456789 // 9 [8] 7 [6] 5 [4] // here we multiply 8 * 2, then 6 * 2, then 4 * 2
            multiplied_number = int(c) * 2
            # for those even numbers, new variable j becomes string elements from values returned from multiplied_number as string for future iteration
            # 456789 // 9 [8] 7 [6] 5 [4] // in 8*2=16, 16 is value of multiplied_number, j=1 and j=6
            for j in str(multiplied_number):
                # sum adds the values of j as int
                sum = sum + int(j)

    # checks if sum is divisible by 10
    if sum % 10 == 0:
        return True
    else:
        return False

def card_bank(card_number):
    # removing all digits of card_number except the first 2
    num = int(str(card_number)[0:2])
    # using conditions to check companies
    if (num == 34 or num == 37) and len(str(card_number)) == 15:
        print("AMEX")
    elif (num > 50 and num <= 55) and len(str(card_number)) == 16:
        print("MASTERCARD")
    elif (num >= 40 and num <50) and (len(str(card_number)) == 13 or len(str(card_number)) == 16):
        print("VISA")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()

# Notes:
# All American Express numbers start with 34 or 37
# Most MasterCard numbers start with 51, 52, 53, 54, or 55 # All Visa numbers start with 4. 
# Credit card numbers also have a “checksum” built into them, a mathematical relationship between at least one number and others. 
# Most cards use an algorithm invented by Hans Peter Luhn of IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:
# Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
# Add the sum to the sum of the digits that weren’t multiplied by 2.
# If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!