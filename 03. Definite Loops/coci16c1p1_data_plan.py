# DMOJ problem coci16c1p1, Data Plan

megabytes_per_month = int(input())
months = int(input())
total = 0

for month in range(months):
	used_megabytes = int(input())
	total = (total + megabytes_per_month) - used_megabytes

print(total + megabytes_per_month)