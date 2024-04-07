# DMOJ problem ac19p1, Darcy's Debilitating Demands

n_t = int(input())

for i in range(n_t):
	n = int(input())
	a = int(input())
	b = int(input())
	c = int(input())

	if b + c >= n:
		a = 0
		if c >= n:
			b = 0
			left_over = c - n 
			c = c - left_over
		else:
			left_over = (b + c) - n 
			b = b - left_over

		print(f"{a} {b} {c}")
	elif a + b + c >= n:	
		left_over = (a + b + c) - n
		a = a - left_over

		print(f"{a} {b} {c}")
	else:
		print(-1)