# 11.DMOJ problem coci20c2p1, Crtanje 

days = int(input())
net_worth = input()
net_worth_changes = []
net_worth_sum = 0

for i in range(days):
	if net_worth[i] == "+":
		net_worth_changes.append([1, net_worth_sum, i])
		net_worth_sum = net_worth_sum + 1
	elif net_worth[i] == "-":
		net_worth_sum = net_worth_sum - 1
		net_worth_changes.append([-1, net_worth_sum, i])
	elif net_worth[i] == '=':
		net_worth_changes.append([0, net_worth_sum, i])

print(net_worth_changes)