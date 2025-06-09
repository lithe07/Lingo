from colorama import *
import random
from lingowords import words
from functies import checkBingo, markBingo, printKaart
from data import *


# Welkom & namen
print("\n🎉 Welkom bij het spel Lingo!")

for i in range(2):
    print(f"\n# Voer de namen in voor {teams[i]}")
    for a in range(2):
        naam = input(f"Naam van speler {a + 1}: ")
        if i == 0:
            team1.append(naam)
        else:
            team2.append(naam)

print("\n👋 Welkom teams!")
print(f"Team 1: {team1[0]} en {team1[1]}")
print(f"Team 2: {team2[0]} en {team2[1]}")


# Start spel
while True:
    print(f"\n {teams[beurt]} is aan de buurt!")

    woord = random.choice(words)
    firstLetter = [woord[0]] + ["_"] * (len(woord)- 1)

    print(f"Nieuw woord! Hint: {woord[0]} {'_ '} * (len(woord) - 1)")
    firstLetter = False

    for poging in range(5):
        gok = input(f"Poging {poging +1} {teams[beurt]}: ").lower()

        if len(gok) != len(woord):
            print("Ongelidig woord, probeer opnieuw.")
            continue

        output = ""
        for i in range(len(woord)):
            if gok[i] == woord[i]:
                output += Fore.GREEN + gok[i] + Style.RESET_ALL
                firstLetter[i] = gok[i]
            elif gok[i] in woord:
                output += Fore.YELLOW + gok[i] + Style.RESET_ALL
            else: output += gok[i]

        print("Resultaat: ", output)
        print("Hint: ", " ".join(firstLetter))

        if gok == woord:
            firstLetter = True
            print(Fore.CYAN + "Goed geredan!" + Style.RESET_ALL)

            teamData[beurt]["goedGeraden"] += 1
            teamData[beurt]["FoutOpRij"] = 0
            print(f"Goed geraden woorden: {teamData[beurt]["goedGeraden"]}")
            print(f"{teams[beurt]} trekt de ballen:")
            nummerGetrokken = False
            eerstBallRood = False

            for grabbel in range(2):
                if grabbel == 1 and eerstBallRood:
                    print("Eerste bal was rood. Geen tweede grabbel toegestaan.")
                    break

                if grabbel == 0:
                    bal = random.choice(ballenBak1)
                    ballenBak1.remove(bal)
                else:
                    bal = random.choice(ballenBak2)
                    ballenBak2.remove(bal)
                print("Getrokken", bal)


                
