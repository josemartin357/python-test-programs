import csv
import sys

def main():
    # Checking for command-line usage
    # argv should include: name_program database_name sequence_name
    if len(sys.argv) != 3:
        print("Command-line argument should include name_program database_name sequence_name")
        sys.exit(1)

    # initial database list
    database = []
    # opening file
    with open(sys.argv[1], 'r') as file:
        # reading database as dictionary
        database_reader = csv.DictReader(file)
        for row in database_reader:
            # adding every row from csv file to database list
            database.append(row)
            
    # opening dna sequence file and reading it
    with open(sys.argv[2], 'r') as file:
        sequence_reader = file.read()

    # strs holds values from database list, the first row index and keys starting from column 2 (skipping name column)
    strs = list(database[0].keys())[1:]

    # Find longest match of each STR in DNA sequence
    # initial empty dictionary for dna sequence
    result = {}
    for str in strs:
        # adding each str (from database) to result dictionary and give each str the value returned by function longest_match applied to dna sequence and each subsequence (str code)
        result[str] = longest_match(sequence_reader, str)

    # Check database for matching profiles
    for person in database:
        matches = 0
        # for every str...
        for str in strs:
            # if the int value of an str in a row in database IS equal to the value of an str from dna sequence
            if int(person[str]) == result[str]:
                # then we give i a new value for the iteration and add 1 to get to the row in database which contains the match
                matches = matches + 1

            
        # If the number of matches equals the length of strs
        if matches == len(strs):
            # then print that person's name
            print(person["name"])
            return

    # if there is no matches, print no match
    print("No match")
    return


   


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            # during the loop, start takes value of i + count (to move right if previously succesful) + value of subsequence_length. This way we itirate from beginning of string, moving right as we loop
            start = i + count * subsequence_length
            # Here we define a proper end which will be the value of start (as it grows right) + subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            # [start:end] removes value of start and end 
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # using max() from python to give longest_run maximum value between longest_run and count
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest_run found
    return longest_run


main()
