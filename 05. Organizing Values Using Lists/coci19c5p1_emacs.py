# 10.DMOJ problem coci19c5p1, Emacs
input_dimensions = input().split()
rows = int(input_dimensions[0])
length = int(input_dimensions[1])
positions = []
count = 0
inp_str = ""

for r in range(rows):
	inp_str = inp_str + input()

if rows == 1:

	for r_2 in range(len(inp_str)):
		if inp_str[r_2] == "*":
			if r_2 == 0:
				count = count + 1
			elif inp_str[r_2-1] == "*":
				count = count
			else:
				count = count + 1

else:

	for i in range(len(inp_str)):
		if inp_str[i] == "*" and i < length:
			if i == 0:
				count = count + 1
				positions.append(i)
			elif inp_str[i-1] == "*":
				count = count
			else:
				count = count + 1
				positions.append(i)
		elif inp_str[i] == "*":
			if inp_str[i-1] == "*" and i % length != 0:
				count = count
			elif i-length in positions:
				positions.append(i)
			else:
				count = count + 1
				positions.append(i)

print(count)
