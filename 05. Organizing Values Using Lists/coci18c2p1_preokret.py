# 3.DMOJ problem coci18c2p1, Preokret

team_1_number = int(input())
all_points = []

for i in range(team_1_number):
	time = int(input())
	all_points.append([time,1])

team_2_number = int(input())

for i in range(team_2_number):
	time = int(input())
	all_points.append([time,2])

all_points.sort()

total_points_team_1 = 0
total_points_team_2 = 0
previous_team = all_points[0][1]
total_turnovers = 0

for i in range(len(all_points)):
	current_team = all_points[i][1]

	if current_team == 1:
		total_points_team_1 = total_points_team_1 + 1
		if current_team != previous_team and total_points_team_1 > total_points_team_2:
			previous_team = current_team
			total_turnovers = total_turnovers + 1
	elif current_team == 2:
		total_points_team_2 = total_points_team_2 + 1
		if current_team != previous_team and total_points_team_1 < total_points_team_2:
			previous_team = current_team
			total_turnovers = total_turnovers + 1

print(len([x for x in all_points if x[0] <= 1440]))
print(total_turnovers)