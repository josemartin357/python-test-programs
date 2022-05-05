# Function outputs the chances of a team winning a tournament. It does so by simulating a tournament 1000 times, and by repeatedly simulating rounds until we are left with one team.

import csv
import sys
import random

# Number of simluations to run
N = 1000

def main():
    # command line argument needs to have 2 inputs. For example: python3 tournament.py 2018m.csv
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    # empty list of teams
    teams = []
    # opening file using argument vector (eg: 2018m.csv), in reading mode. 
    with open(sys.argv[1], "r") as file:
        # variable holds dictionary reader of csv file
        reader = csv.DictReader(file)
        # taking a look at content in dictionary in every row
        for row in reader:
            # variable holds values in row 'team'(defined in csv)
            team_name = row['team']
            # variable converts teams' rating into an int, since all values from csv are strings by standard
            team_rating = int(row['rating'])
            # pushing names and ratings to teams list previously empty and forming team and rating keys
            teams.append({'team':team_name, 'rating': team_rating})
        # print(simulate_tournament(teams))

    # empty dictionary that will eventually hold winning teams as key and a value (times team has won a tournament)
    counts = {}
    # looping to simulate N tournaments 
    for i in range(N):
        # getting name of winning team from value returned in simulate_tournament function
        winner_team = simulate_tournament(teams)
        # if the winner team is already in counts dictionary ...
        if winner_team in counts:
            # ... then every time a team wins, increase counts of that team by 1
            counts[winner_team] += 1
        else:
            # this is the first team has won, so counts for that time equal 1
            counts[winner_team] = 1

    # Print each team's chances of winning, according to simulation
    # sorted sorts teams by counts; key=lambda treats strings as ints to achieve sort, and reverse=true allows to sort in descending order
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        #printing with format string each team AND a formula to obtain percentage with 1 decimal
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")

# function to simulate game takes two arguments
def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    # we grab the ratings by going into the team1 and team2 rating key in dictionary teams (reference function simulate_round)
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    # run probability mathematical equation
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    # random.random() returns a random floating number between 0 and 1
    return random.random() < probability

# function simulates rounds and has teams dictionary being passed on
def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    # start empty list of winners
    winners = []
    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])
    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # if the remaining teams higher than 1 (if there is not just 1 remaining team), keep running round simulation
    while len(teams) > 1:
        # reassigning teams
        teams = simulate_round(teams)
    # otherwise return the remaining team
    return teams[0]['team']



if __name__ == "__main__":
    main()
