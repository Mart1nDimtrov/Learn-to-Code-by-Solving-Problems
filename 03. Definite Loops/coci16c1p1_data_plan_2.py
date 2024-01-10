# DMOJ problem coci16c1p1, Data Plan

megabytes_per_month = int(input())
months = int(input()) 
total = megabytes_per_month * (months + 1)
total_used_megabytes = 0

for month in range(months):
	used_megabytes = int(input())
	total_used_megabytes = total_used_megabytes + used_megabytes

print(total - total_used_megabytes)