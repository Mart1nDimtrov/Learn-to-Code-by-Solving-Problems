# DMOJ problem tc19summerj3, Thor Goes for the Papaya

cipher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n_planets = int(input())
planet = ""
previous = 0

for i in range(n_planets):
	if i == 0:
		previous = int(input())
	else:
		current = int(input())
		index = (previous * current) % 26
		planet = planet + cipher[index]
		previous = current


print(f"Thanos is on Planet: {planet}")
