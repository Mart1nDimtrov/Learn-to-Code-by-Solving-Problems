# DMOJ problem bpc1j1, Cantor Table

n_term = int(input())
count = 0
if n_term == 1:
	print("1/1")
elif n_term == 2:
	print("1/2")
else:
	for i in range(1,n_term):
		temp_count = count

		for j in range(1,i+1):
			if i % 2 == 0:
				temp_count = count + j
			elif i % 2 == 1:
				temp_count = count + ((i - j) + 1)

			if temp_count == n_term:
				print(f"{j}/{i-(j-1)}")
				break

		count = count + i
		if temp_count == n_term:
				break