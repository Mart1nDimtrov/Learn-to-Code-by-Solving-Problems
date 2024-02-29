# DMOJ problem ccc23j1, Deliv-e-droid

packages = int(input())
obstacles = int(input())
if packages > obstacles:
	print(((packages * 50) - (obstacles * 10)) + 500)
else:
	print((packages * 50) - (obstacles * 10))

