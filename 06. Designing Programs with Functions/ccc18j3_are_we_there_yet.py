# 2.DMOJ problem ccc18j3, Are we there yet?

cities = list(map(int, input().split()))

def print_cities(cities, position):

	for j in range(len(cities)+1):
		if j < position:
			print(sum(cities[j:position]), end=" ")
		elif j > position:
			print(sum(cities[position:j]), end=" ")
		else:
			print(0, end=" ")

	print("\n")

for i in range(len(cities)+1):
	print_cities(cities, i)