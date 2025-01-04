# USACO 2019 December Bronze Contest problem Cow Gymnastics

input_file = open('gymnastics.in', 'r')
output_file = open('gymnastics.out', 'w')

line = input_file.readline().split()
practice_sessions = int(line[0])
n_cows = int(line[1])
cow_results = {}

for n_session in range(0, practice_sessions):
	line = list(map(int, input_file.readline().split()))

	for cow_n in range(0, n_cows):
		if n_session == 0:
			cow_results[line[cow_n]] = [0 for x in range(0, n_cows)]
		for cow_n_2 in range(0, n_cows):
			if cow_n < cow_n_2:
				if n_session == 0:
					cow_results[line[cow_n]][line[cow_n_2]-1] = 1
			elif cow_n > cow_n_2:
				cow_results[line[cow_n]][line[cow_n_2]-1] = 0
					
output_file.write(str(sum([sum(value) for key, value in cow_results.items()])))
output_file.close()
input_file.close()
		
