
score = 0
score2 = 0
with open('input-2.txt') as f:
    for line in f.readlines():
        player, me = line.strip().split()
        print(player, me)
        # A for Rock, B for Paper, and C for Scissors.
        # X for Rock, Y for Paper, and Z for Scissors.
        # (1 for Rock, 2 for Paper, and 3 for Scissors)
        win_combination = {
            "A": "Y",
            "B": "Z",
            "C": "X"
        }
        match = {
            "A": "X",
            "B": "Y",
            "C": "Z"
        }
        bonus = {
            "X": 1,
            "Y": 2,
            "Z": 3
        }
        def calc_score(player, me):
            round_score = bonus[me]
            if me == win_combination[player]:
                round_score += 6
            elif me == match[player]:
                round_score += 3
            return round_score
        score += calc_score(player, me)


        # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
        if me == "X":
            move = {
                "A": "Z",
                "B": "X",
                "C": "Y"
            }[player]

        elif me == "Y":
            move = {
                "A": "X",
                "B": "Y",
                "C": "Z"
            }[player]
        elif me == "Z":
            move = win_combination[player]

        score2 += calc_score(player, move)

print(score)
print(score2)
