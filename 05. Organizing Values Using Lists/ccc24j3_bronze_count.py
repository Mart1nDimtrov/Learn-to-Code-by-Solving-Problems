# DMOJ problem ccc24j3, Bronze Count

n = int(input())
participans_list = []

for i in range(n):
	participans_list.append(int(input()))

bronze_score = list(sorted(set(participans_list), reverse=True))[2]
print(f"{bronze_score} {len([p for p in participans_list if p == bronze_score])}")

