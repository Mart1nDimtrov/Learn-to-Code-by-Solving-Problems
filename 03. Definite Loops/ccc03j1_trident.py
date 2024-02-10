# DMOJ problem ccc03j1, Trident

t = int(input())
s = int(input())
h = int(input())

for i in range(t):
	row = "*" + (s * " ") + "*" + (s * " ") + "*" 
	print(row)

print("*" * ((s*2) + 3))

for i_2 in range(h):
	row = ((s + 1) * " ") + "*"
	print(row)
	