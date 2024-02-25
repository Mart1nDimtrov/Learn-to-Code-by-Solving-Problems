# 12.DMOJ problem dmopc19c5p2, Charlie's Crazy Conquest

game_input = input().split()
n_moves = int(game_input[0])
health = int(game_input[1])
c_health = health
o_health = health
move = 0
dodge = 0
damage = 0
c_moves = []
o_moves = []
tie = 1

for i in range(n_moves):
	c_input = input().split()
	c_moves.append([c_input[0], int(c_input[1])])

for i_2 in range(n_moves):
	o_input = input().split()
	o_moves.append([o_input[0], int(o_input[1])])

while n_moves > move:
	if c_moves[move][0] == "A" and dodge == 0:
		o_health = o_health - c_moves[move][1]
		dodge = 0
	elif c_moves[move][0] == "A" and dodge == 1:
		dodge = 0
	elif c_moves[move][0] == "D" and dodge == 1:
		o_health = o_health - damage
		damage = c_moves[move][1]
		dodge = 1
	elif c_moves[move][0] == "D" and dodge == 0:
		damage = c_moves[move][1]
		dodge = 1

	if o_health <= 0:
		print("VICTORY")
		tie = 0
		break
	elif c_health <= 0:
		print("DEFEAT")
		tie = 0
		break

	if o_moves[move][0] == "A" and dodge == 0:
		c_health = c_health - o_moves[move][1]
		dodge = 0
	elif o_moves[move][0] == "A" and dodge == 1:
		dodge = 0
	elif o_moves[move][0] == "D" and move + 1 == n_moves:
		if dodge == 1:
			c_health = c_health - damage
		if o_health <= 0:
			print("VICTORY")
			tie = 0
			break
		elif c_health <= 0:
			print("DEFEAT")
			tie = 0
			break
		o_health = o_health - o_moves[move][1]
	elif o_moves[move][0] == "D" and dodge == 1:
		c_health = c_health - damage
		damage = o_moves[move][1]
		dodge = 1
	elif o_moves[move][0] == "D" and dodge == 0:
		damage = o_moves[move][1]
		dodge = 1

	if o_health <= 0:
		print("VICTORY")
		tie = 0
		break
	elif c_health <= 0:
		print("DEFEAT")
		tie = 0
		break

	move = move + 1

if tie == 1:
	print("TIE")