# program.py

# Imports
from colorama import Fore, Style
import random
import data
from lingoWords import words
from functions import printKaart, markBingo, checkWin

# Welkomsbericht
print("\n🎉 Welkom bij het Lingo spel!")

# Spelersnamen invoeren
for i in range(2):
    print(f"\nVoer de namen in voor {data.teams[i]}")
    for a in range(2):
        while True:
            naam = input(f"Naam van speler {a + 1}: ")
            if not naam:
                print("Naam mag niet leeg zijn.")
            elif not naam.isalpha():
                print("Gebruik alleen letters")
            else:
                break
        if i == 0:
            data.team1.append(naam)
        else:
            data.team2.append(naam)

# Teams tonen
print("\n👋 Welkom teams!")
print(f"Team 1: {data.team1[0]} en {data.team1[1]}")
print(f"Team 2: {data.team2[0]} en {data.team2[1]}")

#-------------------------------------------------------

# Start spelronde
while True:
    print(f"\n{data.teams[data.beurt]} is aan de beurt!")

    woord = random.choice(words)
    goedeLetters = [woord[0]] + ["_"] * (len(woord) - 1)
    print(f"Nieuw woord Hint: {woord[0]} {'_ ' * (len(woord) - 1)}")

    goedGeraden = False
    poging = 0

    while poging < 5:
        gok = input(f"Poging {poging + 1} ({data.teams[data.beurt]}): ").lower()

        if len(gok) != len(woord):
            print("Ongeldig woord, probeer opnieuw.")
            continue
        poging += 1

        # Check letters en toon resultaat
        output = ""
        for i in range(len(woord)):
            if gok[i] == woord[i]:
                output += Fore.GREEN + gok[i]
                goedeLetters[i] = gok[i]
            elif gok[i] in woord:
                output += Fore.YELLOW + gok[i]
            else:
                output += gok[i]
        print("Resultaat:", output)
        print("Hint:", " ".join(goedeLetters))

        if gok == woord:
            print(Fore.GREEN + f"Goed geraden {data.teams[data.beurt]}!")
            data.teamData[data.beurt]["goedGeraden"] += 1
            data.teamData[data.beurt]["foutOpRij"] = 0  # reset foutenreeks

            ballen = data.ballenBak1 if data.beurt == 0 else data.ballenBak2
            eersteBalRood = False
            nummerGetrokken = False

            for i in range(2):
                if i == 1 and eersteBalRood:
                    break

                bal = random.choice(ballen)
                ballen.remove(bal)
                print("Getrokken bal is:", bal)

                if type(bal) == str:
                    if "🟢" in bal:
                        data.teamData[data.beurt]["groen"] += 1
                    elif "🔴" in bal:
                        data.teamData[data.beurt]["rood"] += 1
                        if i == 0:
                            eersteBalRood = True
                elif type(bal) == int:
                    markBingo(data.beurt, bal, data.bingo_kaarten)
                    nummerGetrokken = True

            if nummerGetrokken:
                print(f"\nBingo-kaart van {data.teams[data.beurt]} na ballen:")
                printKaart(data.bingo_kaarten[data.beurt])

            win_bericht = checkWin(data.beurt, data.teams, data.teamData, data.bingo_kaarten)
            if win_bericht:
                print(win_bericht)
                break

            goedGeraden = True
            break

    if not goedGeraden:
        data.teamData[data.beurt]["foutOpRij"] += 1
        print(f"{data.teams[data.beurt]} heeft het woord niet geraden.")
        print(f"Fouten op rij: {data.teamData[data.beurt]['foutOpRij']}")
        win_bericht = checkWin(data.beurt, data.teams, data.teamData, data.bingo_kaarten)
        if win_bericht:
            print(win_bericht)
            break

    # Wissel beurt
    data.beurt = 1 - data.beurt

    # Vraag of gebruiker opnieuw wilt spelen
    opnieuw = input("\nWil je opnieuw spelen? (ja/nee): ").lower()
    if opnieuw != "ja":
        print("Bedankt voor het spelen van Lingo!")
        break