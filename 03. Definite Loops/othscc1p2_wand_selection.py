# DMOJ problem othscc1p2, Wand Selection

n = int(input())
max_element = 0
max_i = 0
elements = []

for i in range(n):
	current = int(input())

	if current > max_element:
		max_element = current
		max_i = i

	elements.append(current)


elements.pop(max_i)
print(sum(elements) // (n - 1))