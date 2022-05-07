# Implement a program that prints out a half-pyramid of a specified height, per the below.

# request user input and run a loop that first requires value and then checks if value is whithin 1 and 8
while True:
    # asking user input as int
    n = int(input("Height: "))
    # if number input is higher/equal or less/equal than 8
    if 1 <= n <= 8:
        # we exit the loop as loop was succesful
        break

# running a loop in i (height) and j (width)
for i in range(n):
    for j in range(n):
        # inside j, we use conditionals for every field and we decide if it will take a # or empty field
        # condition on every field: if the value of i location and j location is higher/equal than value of n-1, then print #
        if i + j >= n-1:
            print("#", end="")
        # else we print empty space
        else:
            print(" ", end="")
    # printing new line
    print()