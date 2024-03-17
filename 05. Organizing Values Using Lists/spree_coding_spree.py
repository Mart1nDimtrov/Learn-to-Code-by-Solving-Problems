# DMOJ problem spree, Coding Spree

def get_maximum_per_element(problems, problem_points, problem_idnex, problem_time, t):
	'''Accept a list, an element,
	a position, and return the maximum sum
	from that position'''

	len_problems = len(problems)
	max_sum = problem_points

	for i in range(len_problems):
		time = problem_time
		current_sum = problem_points

		for j in range(i, len_problems):
			if problem_idnex != j and time + problems[j][1] <= t:
				time = time + problems[j][1]
				current_sum = current_sum + problems[j][0]

		if current_sum > max_sum:
			max_sum = current_sum

	return max_sum


input_params = list(map(int, input().split()))
n = input_params[0]
t = input_params[1]
problems = []

for i in range(n):
	problem_input = list(map(int, input().split()))
	problem_points = problem_input[0]
	problem_time = problem_input[1]
	problems.append([problem_points, problem_time])

problems = [p for p in problems if p[1] <= t]
problems = sorted(problems, key=lambda p: p[1])
problems = sorted(problems, key=lambda p: p[0], reverse=True)

#print(problems)

points_set = []
for i_2 in range(len(problems)):
	points_set.append(get_maximum_per_element(problems, problems[i_2][0], i_2, problems[i_2][1], t))

print(max(points_set))