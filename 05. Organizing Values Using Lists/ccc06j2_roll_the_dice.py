# DMOJ problem ccc06j2, Roll the Dice

dice_1 = int(input())
dice_2 = int(input())
ways = []

for i in range(1, dice_1+1):
	for j in range(1, dice_2+1):
		if (i + j == 10 and [i,j] not in ways):
			ways.append([i,j])

n_ways = len(ways)

if n_ways == 1:
	print(f"There is {n_ways} way to get the sum 10.")
else:
	print(f"There are {n_ways} ways to get the sum 10.")
	


