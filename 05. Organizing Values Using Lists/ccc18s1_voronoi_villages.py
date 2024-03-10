# DMOJ problem ccc18s1, Voronoi Villages

n = int(input())

towns = []

for i in range(n):
	town = int(input())
	towns.append(town)

towns.sort()
n_range = abs(towns[0] - towns[2]) / 2

for i_2 in range(n):
	if i_2 != 0 and i_2 != n - 1:
		current_n = abs(towns[i_2-1] - towns[i_2+1]) / 2
		if current_n < n_range:
			n_range = current_n

print(n_range)
