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
        # print(simulate_tournament(teams))


    counts = {}
    # counts is a dictionary that stores names of teams as keys and values how many tournaments team has won
    # looping to simulate N tournaments and keeping track of win counts
    for i in range(N):
        # getting name of winning team from simulate_tournament function
        winner_team = simulate_tournament(teams)
        if winner_team in counts:
            # every time a team wins, increase counts by 1
            counts[winner_team] += 1
        else:
            # this is the first team has won, so counts equal 1
            counts[winner_team] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
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
