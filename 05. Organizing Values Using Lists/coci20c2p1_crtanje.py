# 11.DMOJ problem coci20c2p1, Crtanje 

days = int(input())
net_worth = input()
net_worth_changes = []
net_worth_sum = 0
max_row = 0
min_row = 0

for i in range(days):
	if net_worth[i] == "+":
		net_worth_changes.append(["/", net_worth_sum, i])
		net_worth_sum = net_worth_sum + 1
	elif net_worth[i] == "-":
		net_worth_sum = net_worth_sum - 1
		net_worth_changes.append(["\\", net_worth_sum, i])
	elif net_worth[i] == '=':
		net_worth_changes.append(["_", net_worth_sum, i])

min_row = min(x[1] for x in net_worth_changes)
max_row = max(x[1] for x in net_worth_changes)

for r in range(max_row, min_row-1, -1):
	for d in range(days):
		if ([x for x in net_worth_changes if x[1] == r and x[2] == d]):
			element = [x[0] for x in net_worth_changes if x[1] == r and x[2] == d][0]
			print(f"{element}", end="")
		else:
			print(f".", end="")
	print("\n")