# DMOJ problem scb24p1, Rock, Paper, Scissors
def check_results(sign, other_sign):
    '''Compare the results for 
    a round of rock, paper, scissors.
    '''

    result = 0

    if sign == other_sign:
        result = 0
    elif sign == "paper":
        if other_sign == "rock":
            result = 1
        else:
            result = -1
    elif sign == "rock":
        if other_sign == "scissors":
            result = 1
        else:
            result = -1
    elif sign == "scissors":
        if other_sign == "paper":
            result = 1
        else:
            result = -1

    return result

n = int(input())
plays = []

for i in range(n):
    plays.append(input())

plays_won = sum([check_results("scissors", x) for x in plays])
plays_won2 = sum([check_results("rock", x) for x in plays])
plays_won3 = sum([check_results("paper", x) for x in plays])

if plays_won > 0 or plays_won2 > 0 or plays_won3 > 0:
    print("yes")
else:
    print("no")