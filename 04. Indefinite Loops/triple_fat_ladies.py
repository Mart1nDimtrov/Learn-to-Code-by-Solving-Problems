# DMOJ problem a3, Triple Fat Ladies

number_of_cases = int(input())

for i in range(number_of_cases):

	k_number = int(input())
	is_triple_eight = 0

	while is_triple_eight == 0:
		k_number = k_number + 1

		if str(k_number**3)[-3:] == "888":
			print(k_number)
			is_triple_eight = 1
