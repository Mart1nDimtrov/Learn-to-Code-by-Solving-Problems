# 2.DMOJ problem ccc15j1, Special Day

month = int(input())
day = int(input())

if day == 18 and month == 2:
	print("Special")
elif day > 18 and month == 2:
	print("After")
elif month > 2:
	print("After")
elif month < 2:
	print("Before")
else:
	print("Before")