# DMOJ problem ccc10j1, What is n, Daddy?

number = int(input())
biggest = 0

for i in range(number):
	for j in range(number):
		if i + j == number:
			if i > biggest or j > biggest:
				biggest = max([i, j])

print(biggest)