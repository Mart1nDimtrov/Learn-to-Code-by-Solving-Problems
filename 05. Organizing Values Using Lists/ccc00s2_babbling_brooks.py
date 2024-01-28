# 4.DMOJ problem ccc00s2, Babbling Brooks

n = int(input())
brooks = []

for i in range(n):
	brook = int(input())
	brooks.append(brook)

action = int(input())

while action != 77:
	stream = int(input())
	if action == 99:
		flow = int(input())

	if action == 99:
		new_brook = int(brooks[stream-1] * (flow / 100))
		brooks[stream-1] = brooks[stream-1] - int(brooks[stream-1] * (flow / 100))
		new_branch = brooks[:stream-1]
		new_branch.append(new_brook)
		brooks = new_branch + brooks[stream-1:]
	elif action == 88:
		brooks[stream-1] = brooks[stream-1] + brooks[stream] 
		brooks = brooks[:stream] + brooks[stream+1:]

	action = int(input())

print(*brooks, sep = " ") 


