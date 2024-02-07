# DMOJ problem wac3p3, Wesley Plays DDR

moves = input()
n_combos = int(input())
l_moves = len(moves)
combos = []
moves_copy = [moves]
for i in range(n_combos):
	combo_input = input().split()
	move = combo_input[0]
	points = int(combo_input[1])
	combos.append([move, points])


total = 0
i = 0
index = 0
end = 0
previous_longest = 0

for i_2 in range(len(moves)):
	if combos[i_2][0] == moves[0:len(combos[i_2])+1]:
		if previous_longest < len(combos[i_2][0]):
			previous_longest = len(combos[i_2][0])
			i = i_2

if previous_longest == 0:
	i = 1


while i < len(combos):

	if len(combos[i][0]) > len(moves):
		break

	if combos[i][0] in moves:
		total = total + combos[i][1]
		index = moves.index(combos[i][0])
		end = index + len(combos[i][0])
		if end > len(moves):
			break
		moves = moves[end:]
		i = i
	else:
		i = i + 1

#if total + l_moves == 86592:
#	print(i_2, previous_longest, combos[i-2], combos[i-3])
print(total + l_moves)