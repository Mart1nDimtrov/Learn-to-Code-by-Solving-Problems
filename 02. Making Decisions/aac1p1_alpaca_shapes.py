# DMOJ problem aac1p1, Alpaca Shapes

parameters_input = input().split()

s = int(parameters_input[0])
r = int(parameters_input[1])

if s**2 > r**2 * 3.14:
	print("SQUARE")
else:
	print("CIRCLE")

