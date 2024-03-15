# DMOJ problem wc18c3j3, R

n = int(input())

for i in range(n):
	if i == 0:
		print(("#" * (n - 1)) + ".")
	elif i != 0 and i != n - 1:
		print("#" + ((n - 2) * ".") + "#")
	elif i == n - 1:
		print(("#" * (n - 1)) + ".")


for i_2 in range(n - 1):
	print("#" + (i_2 * ".") + "#" + ((n - 2 - i_2) * "."))
	