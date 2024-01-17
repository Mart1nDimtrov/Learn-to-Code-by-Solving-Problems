# 4.DMOJ problem ecoo13r1p1, Take a Number

number = int(input())
command = input()
total = number
current_waiting = 0
total_waiting = 0

while command != "EOF":
	if command == "TAKE":
		if total + 1 > 999:
			total = 1
		else:
			total = total + 1
		total_waiting = total_waiting + 1
		current_waiting = current_waiting + 1
	elif command == "SERVE":
		current_waiting = current_waiting - 1
	elif command == "CLOSE":
		print(total_waiting, current_waiting, total)
		current_waiting = 0
		total_waiting = 0

	command = input()



