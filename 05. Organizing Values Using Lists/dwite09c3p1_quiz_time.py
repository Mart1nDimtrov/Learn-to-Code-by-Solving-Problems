# DMOJ problem dwite09c3p1, Quiz Time

questions = {}

for i in range(5):
	question = input()
	row = int(input())
	questions[row] = question

for i_2 in range(1, 6):
	print(questions[i_2])
