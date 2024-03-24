# DMOJ problem aac2p2, Koala Party

def check_for_three_cookies(bowl, index, cookies):
	'''Receive the mean of cookies 
	and cookies and return the evened
	out cookies as a list'''

	is_three = 0
	is_two = 0
	indexes = []
	for i in range(len(cookies)):
		if i != index:
			other_bowl_index = -1
			bowl_difference = bowl - cookies[i]
			other_bowl_index = max([cookies.index(c) for c in cookies if c - bowl_difference == bowl], default=-1)
			if other_bowl_index != -1:
				indexes.append([index, i, other_bowl_index])
				is_three = 1
			if is_three == 0:
				if bowl + cookies[i] % 2 == 0:
					is_two == 1


	return [is_three, is_two]

n_cookies = int(input())
cookies = list(map(int, input().split()))
is_three = 0

for i in range(len(cookies)):
	cookie_check_results = check_for_three_cookies(cookies[i], i, cookies)
	if cookie_check_results[0] == 1:
		is_three = 1
	elif cookie_check_results[0] == 0:
		is_two = 1

if len(cookies) == 2:
	if ((cookies[0] + cookies[1]) % 2 == 0):
		print(2)
	else:
		print(1)
else:
	if is_three == 1:
		print(3)
	elif is_two == 1:
		print(2)
