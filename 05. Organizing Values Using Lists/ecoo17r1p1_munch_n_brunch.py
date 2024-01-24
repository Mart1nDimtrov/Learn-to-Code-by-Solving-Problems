# DMOJ problem ecoo17r1p1, Munch 'n' Brunch

count = 0
prices = [12, 10, 7, 5]

while count < 10:
	cost = int(input())
	percentages = list(map(float, input().split(" ")))
	students = int(input())
	percentages_sum = 0
	counted = 0
	uncounted = 0

	for i in range(4):
		if i == 0:
			#students_rounded = students_rounded + round(((percentages[i] * students) % 1))
			percentages_sum = percentages_sum + (int(percentages[i] * students) * 12)
			counted = counted + int(percentages[i] * students)
		elif i == 1:
			#students_rounded = students_rounded + round(((percentages[i] * students) % 1))
			percentages_sum = percentages_sum + (int(percentages[i] * students) * 10)
			counted = counted + int(percentages[i] * students)
		elif i == 2:
			#students_rounded = students_rounded + round(((percentages[i] * students) % 1))
			percentages_sum = percentages_sum + (int(percentages[i] * students) * 7)
			counted = counted + int(percentages[i] * students)
		elif i == 3:
			counted = counted + int(percentages[i] * students)
			percentages_sum = percentages_sum + ((int(percentages[i] * students) * 5)

	uncounted = students - counted
	percentages_sum = percentages_sum +

	#print(percentages_sum)
	count = count + 1

	if percentages_sum / 2 < cost:
		print("YES")
	else:
		print("NO")