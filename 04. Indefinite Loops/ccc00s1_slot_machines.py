# DMOJ problem ccc00s1, Slot Machines

quarters = int(input())
first_machine = int(input())
second_machine = int(input())
third_machine = int(input())
plays = 0

while quarters > 0:
	for i in range(3):
		if i == 0:
			first_machine = first_machine + 1
		elif i == 1:
			second_machine = second_machine + 1
		elif i == 2:
			third_machine = third_machine + 1

		if i == 0 and first_machine % 35 == 0:
			quarters = quarters + 30
		elif i == 1 and second_machine % 100 == 0:
			quarters = quarters + 60
		elif i == 2 and third_machine % 10 == 0:
			quarters = quarters + 9

		plays = plays + 1
		quarters = quarters - 1

		if quarters <= 0:
			break

print(f"Martha plays {plays} times before going broke.")