# DMOJ problem ccc14j3, Double Dice

dice_rolls_num = int(input())
a_points = 100
b_points = 100
dice_turn = "a"
previous_dice_roll = []

for i in range(dice_rolls_num):
	dice_roll = list(map(int, input().split()))
	if dice_roll[0] > dice_roll[1]:
		b_points = b_points - max(dice_roll)
	elif dice_roll[0] < dice_roll[1]:
		a_points = a_points - max(dice_roll)

print(a_points)
print(b_points)