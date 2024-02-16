# DMOJ problem bf1, List Minimum

n_numbers = int(input())
numbers = []

for i in range(n_numbers):
	numbers.append(int(input()))

numbers.sort()
[print(f"{x}", end="\n") for x in numbers]