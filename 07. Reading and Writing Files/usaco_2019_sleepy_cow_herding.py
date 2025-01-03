# USACO 2019 February Bronze Contest problem Sleepy Cow Herding

def count_cow_moves(cow_positions):
	"""Get a list of the positions and 
	change the list"""
	cow_positions = sorted(cow_positions)
	min_cow_moves = 0
	max_cow_moves = 0
	first_cow_positions = abs(cow_positions[0] - cow_positions[1])
	second_cow_positions = abs(cow_positions[1] - cow_positions[2])

	if first_cow_positions == 1 and second_cow_positions == 1:
		return min_cow_moves, max_cow_moves
	elif first_cow_positions == 2 or second_cow_positions == 2:
		min_cow_moves = 1
	elif first_cow_positions > 2 or second_cow_positions > 2:
		min_cow_moves = 2

	if first_cow_positions > second_cow_positions:
		max_cow_moves = abs(cow_positions[0] - cow_positions[1]) - 1
	elif first_cow_positions < second_cow_positions:
		max_cow_moves = abs(cow_positions[1] - cow_positions[2]) - 1
	else:
		max_cow_moves = abs(cow_positions[1] - cow_positions[2]) - 1

	return min_cow_moves, max_cow_moves



input_file = open('herding.in', 'r')
output_file = open('herding.out', 'w')
cow_positions =list(map(int, input_file.read().split()))
print(cow_positions)
min_cow_moves = 0
max_cow_moves = 0

min_cow_moves, max_cow_moves = count_cow_moves(cow_positions)

print(min_cow_moves, max_cow_moves)

