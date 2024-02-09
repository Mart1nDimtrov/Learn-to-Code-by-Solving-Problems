# DMOJ problem ccc00j1, Calendar
import math

calendar_input = input().split()

start = int(calendar_input[0])
days = int(calendar_input[1])
rows = math.ceil((start + days) / 7)
count = 0
start_count = 0

for row in range(rows):
	if row == 0:
		print("Sun Mon Tue Wed Thr Fri Sat")
	for day in range(1,8):
		if day == start and row == 0:
			start_count = 1

		if count < days and start_count == 1:
			count = count + 1
			if count < 10:
				if day == 7:
					print(f"  {count}", end="\n")
				else:
					print(f"  {count}", end=" ")
			else:
				if day == 7 or count == days:
					print(f" {count}", end="\n")
				else:
					print(f" {count}", end=" ")

		if start_count == 0:
			print("    ", end="")
