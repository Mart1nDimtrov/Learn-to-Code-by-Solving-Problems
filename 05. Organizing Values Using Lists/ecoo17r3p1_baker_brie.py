# DMOJ problem ecoo17r3p1, Baker Brie

for i in range(10):
	inp = list(map(int, input().split(" ")))
	num_franchises = inp[0]
	days = inp[1]
	sum_of_dozens = 0
	franchises_days = []
	for day in range(days):
		franchises_days.append(list(map(int, input().split(" "))))
		if sum(franchises_days[day]) % 13 == 0:
			sum_of_dozens = sum_of_dozens + (sum(franchises_days[day]) // 13)

	for i in (range(num_franchises)):
		fran_sum = 0
		for day_2 in range(days):
			fran_sum = fran_sum + franchises_days[day_2][i]

		if fran_sum % 13 == 0:
			sum_of_dozens = sum_of_dozens + (fran_sum // 13)

	print(sum_of_dozens)
