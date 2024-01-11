# 4.DMOJ problem ccc11s2, Multiple Choice

number_of_lines = int(input())
rows = number_of_lines * 2
score = 0
sheet = ""

for i in range(rows):
	answer = input()
	sheet = sheet + answer
	if (i > number_of_lines - 1):
		if sheet[i] == sheet[i - number_of_lines]:
			score = score + 1

print(score)


