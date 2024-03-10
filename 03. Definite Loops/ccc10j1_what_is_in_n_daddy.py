# DMOJ problem ccc10j1, What is n, Daddy?

number = int(input())
count = 0
bigger = 0
addens = []

for i in range(number):
	for j in range(1,number+1):
		if (i + j == number and
			 (i not in addens or j not in addens)):
			if i >= 5 or j >= 5 and bigger == 1:
				break
			elif i >= 5 or j >= 5:
				bigger = 1

			addens.append(i)
			addens.append(j)
			count = count + 1
			#print(i,j)


print(count)