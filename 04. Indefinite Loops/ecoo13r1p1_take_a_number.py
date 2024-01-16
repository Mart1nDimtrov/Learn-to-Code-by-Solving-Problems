# 4.DMOJ problem ecoo13r1p1, Take a Number

number = int(input())
command = input()
total = 0
waiting = 0
served = 0

while command != "EOF":
	if command == "TAKE":
		waiting = waiting + 1
	elif command == "SERVE":
		served = served + 1
		total = total + 1
		waiting = waiting - 1
	elif command == "CLOSE":
		total = total + waiting
		print(waiting, served - waiting)
		waiting = 0
		served = 0

	command = input()

print(total)


