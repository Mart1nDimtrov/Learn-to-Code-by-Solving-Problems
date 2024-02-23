# DMOJ problem bsspc21j1, Eggy's New Clothes

s = int(input())
x = int(input())

if x >= (((s + 2) * 3) + 16):
	print("Yes it fits!")
else:
	print("No, it's too small :(")