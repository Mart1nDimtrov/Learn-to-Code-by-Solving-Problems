# DMOJ problem a4b1, Sorting

n = int(input())
numbers = []

for i in range(n):
	numbers.append(int(input()))

numbers.sort()
[print(f"{x}", end="\n") for x in numbers]