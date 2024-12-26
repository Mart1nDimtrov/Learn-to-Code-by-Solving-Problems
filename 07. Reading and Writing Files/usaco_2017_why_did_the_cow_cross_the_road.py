# USACO 2017 February Bronze Contest problem Why Did the Cow Cross the Road

input_file = open('crossroad.in', 'r')
output_file = open('crossroad.out', 'w')

n_cows = 0
crossings = []
n_crossings = 0

n_cows = int(input_file.readline())

for i in range(0, n_cows):
	line = input_file.readline().split()
	crossings.append(line)

crossings = sorted(crossings, key=lambda x : x[0])

for i_2 in range(0, n_cows):
	if i_2 > 0 and crossings[i_2][0] == crossings[i_2-1][0] and crossings[i_2][1] != crossings[i_2-1][1]:
		n_crossings = n_crossings + 1

print(n_crossings)
