# 7.DMOJ problem dmopc14c7p2, Tides

waves = int(input())
tide = list(map(int, input().split(" ")))
high_tide = 0
previous = tide[0]
is_unknown = 0

for i in range(waves):

	if previous < tide[i]:
		previous = tide[i]
		high_tide = 1
	elif tide[i] < previous and high_tide == 1:
		is_unknown = 1

if is_unknown:
	print("unknown")
else:
	print(max(tide) - min(tide))




