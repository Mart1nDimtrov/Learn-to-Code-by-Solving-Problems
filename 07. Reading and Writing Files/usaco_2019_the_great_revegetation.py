# USACO 2019 February Bronze Contest problem The Great Revegetation

# Main Program

def find_grass_types_for_pastures(cows):
	'''Find all the pastures related to cows
	and return a list with grass_types.'''

	grass_types = []

	for c in cows:
		grass_types.append(pastures[c[0]])
		grass_types.append(pastures[c[1]])

	return grass_types

input_file = open('revegetate.in', 'r')
output_file = open('revegetate.out', 'w')

input_params = input_file.readline().split()
n_pastures = int(input_params[0])
n_cows = int(input_params[1])

cows = []
pastures = [0 for x in range(n_pastures)]
bucket_seeds = [1, 2, 3, 4]

for i in range(n_cows):
	cow = list(map(int, input_file.readline().split()))
	cow_pasture_1 = cow[0] - 1
	cow_pasture_2 = cow[1] - 1
	cows.append([cow_pasture_1, cow_pasture_2])

for p_i in range(n_pastures):
	cows_for_pasture = [c for c in cows if c[0] == p_i or c[1] == p_i]
	grass_types_for_cows = find_grass_types_for_pastures(cows_for_pasture)
	min_grass_type = min([bucket_seed for bucket_seed in bucket_seeds if bucket_seed not in grass_types_for_cows])
	pastures[p_i] = min_grass_type

output_file.write("".join(map(str, pastures)))
input_file.close()
output_file.close()