# DMOJ problem ccc24j2, Dusa And The Yobis

dusa_size = int(input())
yobi_size = int(input())

while dusa_size > yobi_size:
	dusa_size = dusa_size + yobi_size
	yobi_size = int(input())
	

print(dusa_size)