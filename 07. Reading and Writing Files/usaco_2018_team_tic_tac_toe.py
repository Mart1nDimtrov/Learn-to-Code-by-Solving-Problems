# USACO 2018 US Open Bronze Contest problem Team Tic Tac Toe

input_file = open('tttt.in', 'r')
output_file = open('tttt.out', 'w')
tic_tac_toe_board = []
individual_cows_set = set()
two_cows_set = set()

for i in range(0, 3):
	line = input_file.readline().strip()
	tic_tac_toe_board.append(line)
	if len(set(line)) == 1:
		individual_cows_set.add("".join(set(line)))
		print(individual_cows_set)
	elif len(set(line)) == 2:
		two_cows_set.add("".join(sorted(set(line))))

print(set(tic_tac_toe_board[0][1] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][1]))
print("".join(sorted(set(tic_tac_toe_board[0][1] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][1]))))
print(two_cows_set)

if len(set(tic_tac_toe_board[0][0] + tic_tac_toe_board[1][0] + tic_tac_toe_board[2][0])) == 1:
	individual_cows_set.add("".join(sorted(set(tic_tac_toe_board[0][0] + tic_tac_toe_board[1][0] + tic_tac_toe_board[2][0]))))
if len(set(tic_tac_toe_board[0][1] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][1])) == 1:
	individual_cows_set.add("".join(sorted(set(tic_tac_toe_board[0][1] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][1]))))
if len(set(tic_tac_toe_board[0][2] + tic_tac_toe_board[1][2] + tic_tac_toe_board[2][2])) == 1:
	individual_cows_set.add("".join(sorted(set(tic_tac_toe_board[0][2] + tic_tac_toe_board[1][2] + tic_tac_toe_board[2][2]))))
if len(set(tic_tac_toe_board[0][0] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][2])) == 1:
	individual_cows_set.add("".join(sorted(set(tic_tac_toe_board[0][0] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][2]))))
if len(set(tic_tac_toe_board[0][2] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][0])) == 1:
	individual_cows_set.add("".join(sorted(set(tic_tac_toe_board[0][2] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][0]))))


if len(set(tic_tac_toe_board[0][0] + tic_tac_toe_board[1][0] + tic_tac_toe_board[2][0])) == 2:
	two_cows_set.add("".join(sorted(set(tic_tac_toe_board[0][0] + tic_tac_toe_board[1][0] + tic_tac_toe_board[2][0]))))
if len(set(tic_tac_toe_board[0][1] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][1])) == 2:
	two_cows_set.add("".join(sorted(set(tic_tac_toe_board[0][1] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][1]))))
if len(set(tic_tac_toe_board[0][2] + tic_tac_toe_board[1][2] + tic_tac_toe_board[2][2])) == 2:
	two_cows_set.add("".join(sorted(set(tic_tac_toe_board[0][2] + tic_tac_toe_board[1][2] + tic_tac_toe_board[2][2]))))
if len(set(tic_tac_toe_board[0][0] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][2])) == 2:
	two_cows_set.add("".join(sorted(set(tic_tac_toe_board[0][0] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][2]))))
if len(set(tic_tac_toe_board[0][2] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][0])) == 2:
	two_cows_set.add("".join(sorted(set(tic_tac_toe_board[0][2] + tic_tac_toe_board[1][1] + tic_tac_toe_board[2][0]))))

print(len(individual_cows_set))
print(len(two_cows_set))


