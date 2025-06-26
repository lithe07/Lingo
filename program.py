from colorama import Fore, Style
import random
import data
from lingoWords import words
from functions import printKaart, markBingo, checkWin
from data import reset_data


def start_spel():
    print("\n🎉 Welkom bij het spel Lingo!")

    for i in range(2):
        print(f"\n# Voer de namen in voor {data.teams[i]}")
        for a in range(2):
            while True:
                naam = input(f"Naam van speler {a + 1}: ")
                if not naam:
                    print("❗️ Naam mag niet leeg zijn.")
                elif not naam.isalpha():
                    print("❗️ Gebruik alleen letters")
                else:
                    break
            if i == 0:
                data.team1.append(naam)
            else:
                data.team2.append(naam)

    print("\n👋 Welkom teams!")
    print(f"Team 1: {data.team1[0]} en {data.team1[1]}")
    print(f"Team 2: {data.team2[0]} en {data.team2[1]}")

    while True:
        print(f"\n🎯 {data.teams[data.beurt]} is aan de beurt!")

        woord = "lijst"
        goede_letters = [woord[0]] + ["_"] * (len(woord) - 1)

        print(f"Nieuw woord! Hint: {woord[0]} {'_ ' * (len(woord) - 1)}")

        goed_geraden = False
        poging = 0

        while poging < 5:
            gok = input(f"Poging {poging + 1} ({data.teams[data.beurt]}): ").lower()

            if len(gok) != len(woord):
                print("❗ Ongeldig woord, probeer opnieuw.")
                continue

            poging += 1

            output = ""
            for i in range(len(woord)):
                if gok[i] == woord[i]:
                    output += Fore.GREEN + gok[i] + Style.RESET_ALL
                    goede_letters[i] = gok[i]
                elif gok[i] in woord:
                    output += Fore.YELLOW + gok[i] + Style.RESET_ALL
                else:
                    output += gok[i]

            print("Resultaat:", output)
            print("Huidige hint:", " ".join(goede_letters))

            if gok == woord:
                print(Fore.GREEN + f"🎉 Goed gedaan {data.teams[data.beurt]}!" + Style.RESET_ALL)
                data.teamData[data.beurt]["goedGeraden"] += 1
                data.teamData[data.beurt]["foutOpRij"] = 0

                ballen = data.ballenBak1 if data.beurt == 0 else data.ballenBak2
                eerste_was_rood = False
                nummer_getrokken = False

                for i in range(2):
                    if i == 1 and eerste_was_rood:
                        break

                    bal = random.choice(ballen)
                    ballen.remove(bal)

                    print("🎱 De Getrokken bal is:", bal)

                    if type(bal) == str:
                        if "🟢" in bal:
                            data.teamData[data.beurt]["groen"] += 1
                        elif "🔴" in bal:
                            data.teamData[data.beurt]["rood"] += 1
                            if i == 0:
                                eerste_was_rood = True
                    elif type(bal) == int:
                        markBingo(data.beurt, bal, data.bingo_kaarten)
                        nummer_getrokken = True

                if nummer_getrokken:
                    print(f"\n📋 Bingo-kaart van {data.teams[data.beurt]} na ballen:")
                    printKaart(data.bingo_kaarten[data.beurt])

                win_bericht = checkWin(data.beurt, data.teams, data.teamData, data.bingo_kaarten)
                if win_bericht:
                    print(win_bericht)
                    return

                goed_geraden = True
                break

        if not goed_geraden:
            data.teamData[data.beurt]["foutOpRij"] += 1
            print(f"🚫 {data.teams[data.beurt]} heeft het woord niet geraden.")
            print(f"❗ Fouten op rij: {data.teamData[data.beurt]['foutOpRij']}")
            verlies_bericht = checkWin(data.beurt, data.teams, data.teamData, data.bingo_kaarten)
            if verlies_bericht:
                print(verlies_bericht)
                return

        data.beurt = 1 - data.beurt

# 🔁 Hoofdloop van het spel
while True:
    reset_data()
    start_spel()
    opnieuw = input("\n🔁 Wil je opnieuw spelen? (ja/nee): ").lower()
    if opnieuw != "ja":
        print("Bedankt voor het spelen van Lingo!")
        break