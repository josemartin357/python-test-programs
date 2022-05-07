# Implement a program that prints out a double half-pyramid of a specified height, per the below.

while True:
    # asking user input as int
    n = int(input("Height: "))
    # if number input is higher/equal or less/equal than 8
    if 1 <= n <= 8:
        # we exit the loop as loop was succesful
        break

# running loop for every line
for i in range(n):
    # printing # and empty fields; and using n as reference for logic
    print(" " * (n - i - 1), end="")
    print("#" * (i + 1), end="")
    print(" " * 2, end="")
    print("#" * (i + 1), end="")
    # printing new line
    print()