# DMOJ problem wac3p3, Wesley Plays DDR

moves = input()
n_combos = int(input())
l_moves = len(moves)
combos = []

for i in range(n_combos):
	combo_input = input().split()
	move = combo_input[0]
	points = int(combo_input[1])
	combos.append([move, points])

combos.sort(key=lambda x: len(x[0]), reverse=True)
l_combos = len(combos)
total = 0
i = 0

while i < len(moves):
	has_match = 0
	for j in range(l_combos):
		l_combo = len(combos[j][0])
		end = i + l_combo
		if combos[j][0] == moves[i:end]:
			has_match = 1
			total = total + combos[j][1]
			i = i + l_combo
			break

	if has_match == 0:
		i = i + 1

print(total + l_moves)