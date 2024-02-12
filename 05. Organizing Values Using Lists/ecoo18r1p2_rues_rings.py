# DMOJ problem ecoo18r1p2, Rue's Rings

for d in range(10):
	
	n_routes = int(input())
	possible_routes = []
	for i in range(n_routes):
		route = list(map(int, input().split()))
		n_rout = route[0]
		min_roundabout = min([r for r in route[2:]])

		if i == 0:
			possible_routes = [[n_rout,min_roundabout]]
		else:
			if min_roundabout < possible_routes[0][1]:
				possible_routes = [[n_rout, min_roundabout]]
			elif min_roundabout == possible_routes[0][1]:
				possible_routes.append([n_rout, min_roundabout])

	print(f"{possible_routes[0][1]}",
		 "{" + ",".join(str(pr[0]) for pr in sorted(possible_routes)) + "}")