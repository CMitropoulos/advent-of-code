# A for Rock, B for Paper, and C for Scissors
#  X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors 
# 0 if you lost, 3 if the round was a draw, and 6 if you won 
def part_1(filename):
    i_win_combos = {"A Y", "B Z", "C X"}
    i_lose_combos = {"A Z", "B X", "C Y"}
    draw_combos = {"A X", "B Y", "C Z"}
    score_per_choice = {"X": 1, "Y": 2, "Z": 3}
    score = 0
    with open(filename, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        opp, me = line.split(" ")
        score+= score_per_choice[me]
        if line in i_win_combos:
            score+=6
            print("win",line, score)
        elif line in draw_combos:
            score+=3
            print("draw", line, score)
        else:
            print("loss", line, score)
        
    print(score)


def part_2(filename):

    # A for Rock, B for Paper, and C for Scissors
    #  X need to lose, Y for draw, and Z for win
    # 1 for Rock, 2 for Paper, and 3 for Scissors 
    # 0 if you lost, 3 if the round was a draw, and 6 if you won 
    i_win_combos = {"A":"B", "B":"C", "C": "A"}
    i_lose_combos = {"A": "C", "B": "A", "C": "B"}
    
    score_per_choice = {"A": 1, "B": 2, "C": 3}
    score = 0
    with open(filename, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        opp, result = line.split(" ")    
        if result == "X": #need to lose
            score+=score_per_choice[i_lose_combos[opp]]
        elif result == "Z": #need to win
            score+=score_per_choice[i_win_combos[opp]]
            score+=6
        elif result == "Y":
            score+=score_per_choice[opp]
            score+=3
    print(score)

part_2("./input.txt")
