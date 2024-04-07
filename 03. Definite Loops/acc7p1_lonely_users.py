# DMOJ problem acc7p1, Lonely Users

n_c = int(input())

for i in range(n_c):
	n = int(input())
	
	if n == 2:
		print(2)
	else:
		print(n - 1)
