# DMOJ problem ccc12s1, Don't pass me the ball!

jersey_n = int(input())
count = 0

for i in range(1, jersey_n):
	for j in range(i+1, jersey_n):
		for k in range(j+1, jersey_n):
			count = count + 1

print(count)

