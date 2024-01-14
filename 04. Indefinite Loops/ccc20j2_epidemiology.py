# 1.DMOJ problem ccc20j2, Epidemiology
total_people = int(input())
current_people = int(input())
rate = int(input())
days = 0
current_rate = 0

while total_people >= current_people:
	if days == 0:
		current_rate = rate * current_people 
	else:
		current_rate = current_rate * rate 
	current_people = current_people + current_rate
	days = days + 1

print(days)


