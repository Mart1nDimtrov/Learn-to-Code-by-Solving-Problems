# 7.DMOJ problem dmopc14c7p2, Tides

waves = int(input())
tide = list(map(int, input().split(" ")))

min_low_tide_value = min(tide)
max_high_tide_value = max([x for x in tide])
min_low_tide_i = tide.index(min(tide))
max_high_tide_i = tide.index(max([x for x in tide]))
current = 0
unknown = 0

if min_low_tide_i + 1 < len(tide):
	current = tide[min_low_tide_i + 1]
	if min_low_tide_i > max_high_tide_i:
		unknown = 1
	else:
		for i in range(min_low_tide_i + 1, max_high_tide_i):
			if current < tide[i]:
				current = tide[i]
			elif current > tide[i]:
				unknown = 1
else:
	unknown = 1
	
if unknown:
	print("unknown")
else:
	print(max_high_tide_value - min_low_tide_value)

