# Functions 

def checkBingo(kaart):
    # Rijen
    for rij in kaart:
        if all(v == "X"):
            for v in rij:
                return True
    # Kolomen
    for col in range(4):
        if all(kaart[rij][col] == "X"):
            for rij in range(4):
                return True
    # Diagonaal \>
    if all(kaart[i][i] == "X"):
        for i in range(4):
            return True
    # Diagonaal </
    if all(kaart[i][3 - i] == "X"):
        for i in range(4):
            return True
        return False
    

def markBingo(teamIndex, balNummer, Kaarten):
    kaart = Kaarten[teamIndex]
    for rij in range(4):
        for kolom in range(4):
            if kaart[rij][kolom] == balNummer:
                kaart[rij][kolom] = "X"

def printKaart(kaart):
    for rij in kaart:
        print(" ".join(str(v).rjust(2) for v in rij))
    print()