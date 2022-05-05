# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000

def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # teams need to read from csv all teams and sort teams inside, so we use a dictionary
    # opening file using argument vector, in reading mode. For example, to run: python3 tournament.py 2018m.csv
    with open(sys.argv[1], "r") as file:
        # turning file into dictionary
        reader = csv.DictReader(file)
        # taking a look at content in dictionary thru every row
        for row in reader:
            # defining variable for row team
            team_name = row['team']
            # new variable converts teams' rating into an int, since all values from csv are strings by standard
            team_rating = int(row['rating'])
            # appending to teams list
            teams.append({'team':team_name, 'rating': team_rating})
        print(teams)
   

    
    # TODO: Need to establish variable counts. It needs to be a dictionary that stores names of teams as keys and values how many tournaments team has won
