# USACO 2017 US Open Bronze Contest problem The Lost Cow

input_file = open('lostcow.in', 'r')
output_file = open('lostcow.out', 'w')

line = input_file.readline().split()
position_farmer = int(line[0])
position_cow = int(line[1])
distance = 1
distance_sum = 0
previous_distance = 0
up = 1

while True:

	distance_sum = distance_sum + (distance + previous_distance)

	if up == 1 and position_cow > position_farmer and position_farmer + distance >= position_cow:
		distance_sum = distance_sum - ((position_farmer + distance) - position_cow)
		break
	elif up == 0 and position_cow < position_farmer and position_farmer - distance <= position_cow:
		distance_sum = distance_sum - (position_cow - (position_farmer - distance))
		break

	if up == 1:
		up = 0
	else:
		up = 1

	previous_distance = distance
	distance = distance * 2

output_file.write(str(distance_sum))
output_file.close()
input_file.close()




