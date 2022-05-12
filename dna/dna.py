import csv
from sys import argv

def main():

    # check for correct number of arguments
    # if correct, we assume we have .csv file in second argument and .txt file in third argument
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    # open database which will be the 2nd argument vector (not counting python3)
    database_file = open("./"+ argv[1])
    # open dna sequence which will be the 3rd argument vector (not counting python3)
    dna_file = open("./" + argv[2])

    # obtain STRs from header of database
    # database_reader becomes a dictionary with data from csv
    database_reader = csv.DictReader(database_file)
    # in database, strs reads fields in first row from second column on: AGATC, AATG, TATC
    strs = database_reader.fieldnames[1:] #1: allows ignoring first field 'name'

    # from dna sequence, we copy contents of dna_file into string dna and close file
    dna = dna_file.read()
    dna_file.close()

    # from database, count number of occurences of each STR is in a dna sequence and store value in dictionary dna_fingerprint{}
    # starting empty dictionary 
    # example of how dna_fingerprint will look: { 'AGATC': 15, 'TTTTTTCT': 49, 'AATG': 38, etc, etc, etc}
    dna_fingerprint = {}
    # iterating thru each strs
    for str in strs:
        # dna_fingerprint stores how many times each str is in a dna sequence
        dna_fingerprint[str] = consec_repeats(str, dna)
        # consec_repeats takes group of letters from str (AGATC for example) and checks how many times in sequence

    # search through each line csv file to find if value matches what's on str
    for row in database_reader:
        # if match function succesful, print name, close files, and end program
        if match(strs, dna_fingerprint, row):
            print(f"{row['name']}")
            database_file.close()
            return

    # if no match was found, print No match and close files.
    print("No match")
    database_file.close()


# repeats determines the maximum number of consecutive repeats of str in dna sequence
# How it works: grab AGATC str and checks if it is in dna sequence. 
def consec_repeats(str, dna):
    # initial value of 0
    i = 0
    # checking if str times i+1 is in dna
    # example: when AGATC (str * 0+1) in dna
    while str*(i+1) in dna:
        # example: i takes value of 1 and loops again until done
        i = i + 1
    return i


# match determines whether dna_fingerprint matches row and strs from database
def match(strs, dna_fingerprint, row):
    for str in strs:
        # comparing each sequence of dna with the row
        if dna_fingerprint[str] != int(row[str]):
            return False
    return True


main()


# NOTES
# Exercise link: https://cs50.harvard.edu/x/2022/psets/6/dna/
# Goal: Program should search thru one of the sequences how many times each str pattern is repeated. Then, it should compare those results with a database and provide as an output the name of the person whose numbers of strs matches the strs in the sequence searched.
# Logic:
# 1 - need to open csv file and dna sequence and read its contents
# 2 - compute how many times each str is repeated in a sequence
# 3 - In a dictionary, save the results including str and its value 
# 4 - compare the values for of the strs row in the database vs sequence
# 5 - output name of person in database whose str count matches the sequence. Otherwise, print no match.
