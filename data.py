# Dat.py

# Teams en Beurt
teams = ["Team 1", "Team 2"]
beurt = 0

# Namen opslaan
team1 = []
team2 = []

# Ballenbak per team
ballenBak1 = ["🟢", "🟢", "🟢", "🔴", "🔴", "🔴", 2, 4, 6, 8, 10, 12, 14, 16]
ballenBak2 = ["🟢", "🟢", "🟢", "🔴", "🔴", "🔴", 1, 3, 5, 7, 9, 13, 15,]


# Team data (per team)
teamData = [
    {"groen": 0, "rood": 0, "goedGeraden": 0, "foutOpRij": 0},
    {"groen": 0, "rood": 0, "goedGeraden": 0, "foutOpRij": 0}
]


# Bingo-kaarten per team
bingo_kaarten = [
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]],

    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
]


# ResetData
def reset_data():
    global beurt, team1, team2, ballenBak1, ballenBak2, teamData, bingo_kaarten

    beurt = 0
    team1.clear()
    team2.clear()

    ballenBak1[:] = ["🟢", "🟢", "🟢", "🔴", "🔴", "🔴", 2, 4, 6, 8, 10, 12, 14, 16]
    ballenBak2[:] = ["🟢", "🟢", "🟢", "🔴", "🔴", "🔴", 1, 3, 5, 7, 9, 13, 15]

    teamData[:] = [
        {"groen": 0, "rood": 0, "goedGeraden": 0, "foutOpRij": 0},
        {"groen": 0, "rood": 0, "goedGeraden": 0, "foutOpRij": 0}
    ]

    bingo_kaarten[:] = [
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]],
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    ]