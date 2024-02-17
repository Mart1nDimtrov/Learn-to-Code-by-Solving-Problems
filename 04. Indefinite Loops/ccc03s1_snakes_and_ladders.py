# DMOJ problem ccc03s1, Snakes and Ladders

position = 1
move = int(input())
snakes = {
	54:19,
	90:48,
	99:77,
}
ladders = {
	9:34,
	40:64,
	67:86,
}

while move != 0:
	if position + move > 100:
		position = position
	else:
		position = position + move

	if position in snakes.keys():
		position = snakes[position]
	elif position in ladders.keys():
		position = ladders[position]


	if position == 100:
		print(f"You are now on square {position}")
		break
	else:
		print(f"You are now on square {position}")

	move = int(input())

if position == 100:
	print("You Win!")
elif move == 0:
	print("You Quit!")
