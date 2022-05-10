from cs50 import get_int

def main():
    while True:
        number = get_int("Bank number: ")
        if number > 0:
            break

    if verify(number):
        printcard(number)
    else:
        print("INVALID")

def verify(number_bank):
    # initial value
    sum = 0
    # reversed version of number_bank
    reversed_number = reversed(str(number_bank))
    # iterating through reversed_number
    for i, number in enumerate(reversed_number):
        # accesing those numbers that will remain intact
        if i % 2 == 0:
            # adding to sum
            sum = sum + int(number)

        # accesing numbers that will be * 2
        else:
            # new variable * 2
            multiply_two = int(number) * 2
            # finding those numbers w/2 digits after being multiplied
            for j in str(multiply_two):
                sum = sum + int(j)

    if sum % 10 == 0:
        return True
    else:
        return False


def printcard(number):
     # removing all digits of card_number except the first 2
    num = int(str(number)[0:2])
    # using conditions to check companies
    if (num == 34 or num == 37) and len(str(number)) == 15:
        print("AMEX")
    elif (num > 50 and num <= 55) and len(str(number)) == 16:
        print("MASTERCARD")
    elif (num >= 40 and num <50) and (len(str(number)) == 13 or len(str(number)) == 16):
        print("VISA")
    else:
        print("INVALID")


main()