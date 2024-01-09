# DMOJ problem ccc18j2, Occupy parking

parking_spaces_number = int(input())
parking_spaces_yesterday = input()
parking_spaces_today = input()
parking_count = 0

for i in range(parking_spaces_number):
	if (parking_spaces_yesterday[i] == parking_spaces_today[i] and
	   parking_spaces_yesterday[i] == "C"):
	   parking_count = parking_count + 1

print(parking_count)
