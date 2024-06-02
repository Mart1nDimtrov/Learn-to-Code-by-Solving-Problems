# DMOJ problem STNBD P1 - Ren Ashbell

n = int(input())
power_levels = []

for i in range(n):
	power_levels.append(int(input()))
 
if power_levels[0] > max(power_levels[1:]):
	print("YES")
else:
	print("NO")
