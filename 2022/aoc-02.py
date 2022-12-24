import sys

names = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

outcome = {
"X": "loose",
"Y": "draw",
"Z": "win",
}

scores = { "X": 1, "Y": 2, "Z": 3}
wins = {
        "A": (3, 6, 0),
        "B": (0, 3, 6),
        "C": (6, 0, 3),
}

expected = {
        "X": ("C", "A", "B"),
        "Y": ("A", "B", "C"),
        "Z": ("B", "C", "A"),
}

cost = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 0,
        "Y": 3,
        "Z": 6,
}

total_score = 0
new_score = 0
for l in sys.stdin:
    opponent = l[0]
    you = l[2]
    your_choice = expected[you][ord(opponent) - ord("A")]
    total_score += scores[you] + wins[opponent][ord(you)-ord("X")]
    new_score += cost[you] + cost[your_choice]
    print(names[opponent], names[you], outcome[you], names[your_choice], total_score, new_score)

print(total_score, new_score)
