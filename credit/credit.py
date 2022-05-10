# write a program that prompts the user for a credit card number and then reports (via print) whether it is a valid American Express, MasterCard, or Visa card number.

from re import I
from cs50 import get_string

def main():
    # First we ask cards number
    card_number = get_string("Enter card number: ")
    check_sum(card_number)
 
# checking if card passes the lunh algorithm
def check_sum(card_number):
    # reverse numbers and save in a new variable reversed_num
    reversed_num = card_number[::-1]

    # TEST: loop to iterate thru reversed_sum and save current_number
    # for i in range(len(reversed_num)):
    #     current_number = reversed_num[i]

    # splitting reversed_num in a list
    array_num = list(reversed_num)
    # converting to int
    ints = [int(item) for item in array_num]
    # start even_num and odd_num with value 0
    even_num = 0
    odd_num = 0
    # identifying the every other digit
    even_list = ints[1::2]
    # identifying odd digits
    odd_list = ints[::2]
    # need to loop thru even_list to * 2
    for i in range(len(even_list)):
        # new list gets index of all values * 2
        multiplied_list = even_list[i] * 2
        print(multiplied_list)

main()

# Notes:
# All American Express numbers start with 34 or 37
# Most MasterCard numbers start with 51, 52, 53, 54, or 55 # All Visa numbers start with 4. 
# Credit card numbers also have a “checksum” built into them, a mathematical relationship between at least one number and others. 
# Most cards use an algorithm invented by Hans Peter Luhn of IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:
# Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
# Add the sum to the sum of the digits that weren’t multiplied by 2.
# If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!