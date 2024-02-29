# DMOJ problem ccc23j1, Deliv-e-droid

packages = int(input())
obstacles = int(input())
result = (packages * 50) - (obstacles * 10)

if packages > obstacles:
	print(result + 500)
else:
	print(result)

