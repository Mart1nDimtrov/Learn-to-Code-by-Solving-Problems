# DMOJ problem sac22cc3jp2, Normal Lines

line_1 = input().split()
line_2 = input().split()

line_1_x = int(line_1[0])
line_1_y = int(line_1[1])
line_2_x = int(line_2[0])
line_2_y = int(line_2[1])

if line_1_x == line_2_x:
	print("y-axis")
elif line_2_y == line_1_y:
	print("x-axis")
else:
	print("neither")

