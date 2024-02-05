# DMOJ problem tc19summerj2, Thanos Knows the Most

thanos_input = input().split()
planets = int(thanos_input[0])
jems = int(thanos_input[1])
close_jems = 0
time = 0

for i in range(planets):
	planet_jems = int(input())

	if planet_jems == 1 and close_jems == 0:
		time = time + 1
		close_jems = 1
	elif planet_jems == 0:
		close_jems = 0

print(time)

