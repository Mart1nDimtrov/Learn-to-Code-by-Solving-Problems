# USACO 2017 US Open Bronze Contest problem Bovine Genomics 

input_file = open('cownomics.in', 'r')
output_file = open('cownomics.out', 'w')

line = input_file.readline().split()
n_genomes = int(line[0])
n_positions = int(line[1])
spotty_cow_genomes = {}
plain_cow_genomes = {}
possible_spotty_genomes_count = 0

for n_genome in range(0, n_genomes):
	line = input_file.readline()
	for position in range(0, n_positions):
		if position not in spotty_cow_genomes.keys():
			spotty_cow_genomes[position] = []
			spotty_cow_genomes[position].append(line[position])
		elif line[position] not in spotty_cow_genomes[position]:
			spotty_cow_genomes[position].append(line[position])

for n_genome in range(0, n_genomes):
	line = input_file.readline()
	for position in range(0, n_positions):
		if position not in plain_cow_genomes.keys():
			plain_cow_genomes[position] = []
			plain_cow_genomes[position].append(line[position])
		elif line[position] not in plain_cow_genomes[position]:
			plain_cow_genomes[position].append(line[position])

for position in range(0, n_positions):
	unique_counter = 0
	for genome_letters_index in range(0, len(spotty_cow_genomes[position])):
		if spotty_cow_genomes[position][genome_letters_index] not in plain_cow_genomes[position]:
			unique_counter = unique_counter + 1
			if unique_counter == len(spotty_cow_genomes[position]):
				possible_spotty_genomes_count = possible_spotty_genomes_count + 1

output_file.write(str(possible_spotty_genomes_count))
output_file.close()
input_file.close()

