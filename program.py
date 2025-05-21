from time import *
from colorama import *


print("\n{Welkom bij het spel Lingo}")

team1 = []
team2 = []

for i in range(2):
    print(f"\n# Voer de namen van team {i +1}")
    for a in range(2):
        teamName = input(f"Naam van de speler {a +1} is: ")
        if i == 0:
            team1.append(teamName)
        else:
            team2.append(teamName)

print("\nWelkom teams!")
print(f"Team 1: {team1[0]} en {team1[1]}")
print(f"Team 2: {team1[0]} en {team1[1]}")
