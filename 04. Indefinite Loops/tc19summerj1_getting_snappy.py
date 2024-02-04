# DMOJ problem tc19summerj1, Getting Snappy

papayas_input = input().split()
n_papayas = int(papayas_input[0])
papaya_meal = int(papayas_input[1])
closest = [n_papayas, n_papayas]

while n_papayas > 0:
	if abs(n_papayas - papaya_meal) < closest[1]:
		closest[0] = n_papayas
		closest[1] = abs(n_papayas - papaya_meal)
	elif (abs(n_papayas - papaya_meal) == closest[1] and 
		  closest[0] < n_papayas):
		closest[0] = n_papayas
	n_papayas = n_papayas // 2

print(closest[0])