# 5.DMOJ problem ecoo18r1p1, Willow’s Wild Ride

for i in range(10):
	parameters = input().split()
	cat_time = int(parameters[0])
	days = int(parameters[1])
	counter = 0
	for day in range(1, days+1):

		play_day = input()

		if play_day == "B":
			counter = counter + cat_time
		
		if counter > 0:
			counter = counter - 1

	print(counter)





		
