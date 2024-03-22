# DMOJ problem aac7p1, Squirrnect 4

boards_n = int(input())

for i in range(boards_n):
	board_input = list(map(int, input().split()))
	w = board_input[0]
	h = board_input[1]

	if w >= 4 and h >= 2:
		print("good")
	elif w >= 7 and h >= 1:
		print("good")
	elif h >= 4 and w >= 2:
		print("good")
	else:
		print("bad")