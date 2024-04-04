# DMOJ problem ccc12j2, Sounds fishy!

depth_1 = int(input())
depth_2 = int(input())
depth_3 = int(input())
depth_4 = int(input())

if depth_1 < depth_2 < depth_3 < depth_4:
	print("Fish Rising") 
elif depth_1 > depth_2 > depth_3 > depth_4:
	print("Fish Diving")
elif depth_1 == depth_2 == depth_3 == depth_4:
	print("Fish At Constant Depth")
else:
	print("No Fish")