# DMOJ problem acc8p1, Trash Push

t = int(input())

for i in range(t):
	fireworks_input = list(map(int, input().split()))
	trash_cans = fireworks_input[0]
	fireworks_wrappers = fireworks_input[1]

	if trash_cans <= fireworks_wrappers:
		print(1)
	else:
		if trash_cans % fireworks_wrappers == 0:
			print(trash_cans // fireworks_wrappers)
		else:
			print((trash_cans // fireworks_wrappers) + 1)
