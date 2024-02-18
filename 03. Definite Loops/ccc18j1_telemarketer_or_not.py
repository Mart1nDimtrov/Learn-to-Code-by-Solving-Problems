# DMOJ problem ccc18j1, Telemarketer or not?

is_telemarketer = 1
previous = 1

for i in range(4):
	digit = int(input())
	if (i == 0 or i == 3) and digit in(8,9) and is_telemarketer == 1:
		is_telemarketer = 1
	elif ((i == 2 and previous == digit) or i == 1) and is_telemarketer == 1:
		is_telemarketer = 1
	else:
		is_telemarketer = 0

	previous = digit

if is_telemarketer == 1:
	print("ignore")
else:
	print("answer")