# 6.DMOJ problem ecoo19r1p1, Free Shirts

for i in range(10):
	
	parameters = input().split()
	shirts = int(parameters[0])
	events_number = int(parameters[1])
	days = int(parameters[2])
	shirts_in_use = shirts
	event_days = list(map(int, input().split(" ")))
	laundry_count = 0

	for day in range(1,days+1):

		if shirts_in_use == 0:
			shirts_in_use = shirts
			laundry_count = laundry_count + 1

		if day in event_days:
			shirts = shirts + len([event_day for event_day in event_days if day == event_day])
			shirts_in_use = shirts_in_use + len([event_day for event_day in event_days if day == event_day])

		shirts_in_use = shirts_in_use - 1

	print(laundry_count)
