from colorama import Fore, Style

# Functions 


def checkBingo(kaart):
    # Controleer horizontaal
    for rij in kaart:
        if all(v == "X" for v in rij):
            return True

    # Controleer verticaal
    for kolom in range(4):
        if all(rij[kolom] == "X" for rij in kaart):
            return True

    # Controleer diagonalen
    if all(kaart[i][i] == "X" for i in range(4)):
        return True
    if all(kaart[i][3 - i] == "X" for i in range(4)):
        return True

    return False
    
# Markeert X op het bingo kaart
def markBingo(teamIndex, balNummer, Kaarten):
    kaart = Kaarten[teamIndex]
    for rij in range(4):
        for kolom in range(4):
            if kaart[rij][kolom] == balNummer:
                kaart[rij][kolom] = "X"

# Print de update versie van het bingo kaar
def printKaart(kaart):
    for rij in kaart:
        print(" ".join(str(v).rjust(2) for v in rij))
    print()



# Checken wie verliest of wint
def checkWin(beurt, teams, team_data, bingo_kaarten):
    if team_data[beurt]["groen"] >= 3:
        return(Fore.GREEN + f"🏆 {teams[beurt]} wint met 3 groene ballen!" + Style.RESET_ALL)
        
    elif team_data[beurt]["rood"] >= 3:
        return(Fore.RED + f"💥 {teams[beurt]} verliest met 3 rode ballen!" + Style.RESET_ALL)
        
    elif team_data[beurt]["goedGeraden"] >= 10:
        return(Fore.GREEN + f"🏆 {teams[beurt]} wint met 10 goed geraden woorden!" + Style.RESET_ALL)
        
    elif team_data[beurt]["foutOpRij"] >= 3:
        return(Fore.RED + f"💥 {teams[beurt]} verliest met 3 fout geraden woorden op rij!" + Style.RESET_ALL)
        
    elif checkBingo(bingo_kaarten[beurt]):
        return(Fore.GREEN + f"🏆 {teams[beurt]} wint met een bingo-lijn!" + Style.RESET_ALL)
        
    return False