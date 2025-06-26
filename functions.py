# Functions

# kleuren importeren 
from colorama import Fore

def checkBingo(kaart):
    # Controleer horizontaal
    for rij in kaart:
        if all(v == "X" for v in rij):
            return True
        
    # Controleer verticaal
    for kolom in range(4):
        if all(rij[kolom] == "X" for i in range(4)):
            return True
        
    # Controleer diagonalen
    if all(kaart[i][i] == "X" for i in range(4)):
        return True
    if all(kaart[i][3 - i] == "X" for i in range(4)):
        return True
    return False


# Markeek X op bingo kaart
def markBingo(teamIndex, balNummer, kaarten):
    kaart = kaarten[teamIndex]
    for rij in range(4):
        for kolom in range(4):
            if kaart[rij][kolom] == balNummer:
                kaart[rij][kolom] = "X"


# Print updadte bingo kaart
def printKaart(kaart): 
    regels = []
    for rij in kaart:
        regel = " ".join(str(v).rjust(2) for v in rij)
        regels.append(regel)
    return "\n".join(regels)  


# Checken wie wint van Teams
def checkWin(beurt, teams, teamData, bingo_kaarten):
    if teamData[beurt]["groen"] == 3:
        return(Fore.GREEN + f"{teams[beurt]} wint met 3 groene ballen!")
    
    elif teamData[beurt]["rood"] == 3:
        return(Fore.RED + f"{teams[beurt]} verliest met 3 rode ballen!")
    
    elif teamData[beurt]["goedGeraden"] == 10:
        return(Fore.GREEN + f"{teams[beurt]} wint met 10 goed geraden woorden!")
    
    elif teamData[beurt]["foutOpRij"] == 3:
        return(Fore.RED + f"{teams[beurt]} verliest met 3 fout geraden woorden op rij!")
    
    elif checkBingo(bingo_kaarten[beurt]):
        return(Fore.GREEN + f"{teams[beurt]} wint met een bingo_lijn!")
               
    return False