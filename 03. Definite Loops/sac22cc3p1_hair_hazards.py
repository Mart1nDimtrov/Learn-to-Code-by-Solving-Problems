# DMOJ problem sac22cc3p1, Hair Hazards

hair_length = int(input())
hair_trimmed = int(input())
n_haircuts = int(input())

for i in range(n_haircuts):
	hair_length = hair_length - hair_trimmed
	print(hair_length)