from functions import checkBingo, markBingo, checkWin

# Test checkBingo
print("Test checkBingo:")
kaart = [
    ["X", "X", "X", "X"],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print("Horizontale bingo:", checkBingo(kaart))  # Verwacht: True

kaart = [
    [1, 2, 3, "X"],
    [5, 6, "X", 8],
    [9, "X", 11, 12],
    ["X", 14, 15, 16]
]
print("Diagonale bingo:", checkBingo(kaart))  # Verwacht: True

kaart = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print("Geen bingo:", checkBingo(kaart))  # Verwacht: False

print()

# Test markBingo
print("Test markBingo:")
kaarten = [[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]]
markBingo(0, 6, kaarten)
print("6 moet X zijn:", kaarten[0][1])  # Verwacht: [5, 'X', 7, 8]

print()

# Test checkWin
print("Test checkWin:")
team_data = [{"groen": 3, "rood": 0, "goedGeraden": 0, "foutOpRij": 0}]
bingo_kaarten = [[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]]
resultaat = checkWin(0, ["Team 1"], team_data, bingo_kaarten)
print("Win met 3 groen:", resultaat)  # Verwacht: iets met "wint met 3 groene ballen"   