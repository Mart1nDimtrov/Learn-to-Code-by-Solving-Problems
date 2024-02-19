# DMOJ problem uhcc1p1, PONG!

players_input = input().split()
x = int(players_input[0])
y = int(players_input[1])
z = int(players_input[2])
l = int(input())
player1_points = 0
player2_points = 0
won = 0

if x >= y:
	player2_points = player2_points + y
	if player2_points >= l and won == 0:
		won = 2
	player1_points = player1_points + z
	if player1_points >= l and won == 0:
		won = 1
elif y > x:
	player1_points = player1_points + x
	if player1_points >= l and won == 0:
		won = 1

while player1_points < l and player2_points < l:
	if player1_points < player2_points:
		player1_points = player1_points + x
		if player1_points >= l and won == 0:
			won = 1
	elif player2_points <= player1_points:
		player2_points = player2_points + y
		if player2_points >= l and won == 0:
			won = 2
		player1_points = player1_points + z
		if player1_points >= l and won == 0:
			won = 1

print(won)