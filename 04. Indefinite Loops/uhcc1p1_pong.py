# DMOJ problem uhcc1p1, PONG!

players_input = input().split()
x = int(players_input[0])
y = int(players_input[1])
z = int(players_input[2])
l = int(input())
player1_points = 0
player2_points = 0
is_won = 0

if x >= y:
	player2_points = player2_points + y
	player1_points = player1_points + z
	if player2_points > l:
		is_won = 1
		print(2)
	if player1_points > l:
		is_won = 1
		print(1)
elif y > x:
	player1_points = player1_points + x
	if player1_points == l:
		is_won = 1
		print(1)

while player1_points < l and player2_points < l:
	if player1_points < player2_points:
		player1_points = player1_points + x
	elif player2_points <= player1_points:
		player2_points = player2_points + y 
		player1_points = player1_points + z

if is_won == 0:
	if player1_points > player2_points:
		print(1)
	elif player1_points < player2_points:
		print(2)