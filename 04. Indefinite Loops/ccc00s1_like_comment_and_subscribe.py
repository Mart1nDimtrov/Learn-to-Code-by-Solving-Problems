# DMOJ problem ccc00s1, Like, Comment, and Subscribe!

x = int(input())
x_copy = x
is_power_of_10 = 0

while is_power_of_10 == 0:
	x = x + 1
	if x % 10 == 0:
		if str(x).replace("0", "") == "1":
			is_power_of_10 = 1

print(x - x_copy)


