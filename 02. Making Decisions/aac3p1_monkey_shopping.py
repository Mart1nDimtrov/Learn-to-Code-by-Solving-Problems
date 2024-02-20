# DMOJ problem aac3p1, Monkey Shopping

units_input = input().split()
a = int(units_input[0])
b = int(units_input[1])
c = int(units_input[2])
d = int(units_input[3])

if (a < b) and (c < d):
	print("Go to the department store")
elif (a >= b) and (c < d):
	print("Go to the pharmacy")
elif (a < b) and (c >= d):
	print("Go to the grocery store")
else:
	print("Stay home")