# DMOJ problem ccc18j2, Bamboo Cookies 

n_batches = int(input())
cookies = list(map(int, input().split()))
cookie_pairs_count = 0

for i in range(n_batches):
	for j in range(i+1,n_batches):
		if ((cookies[i] + cookies[j]) % 2 == 0 and
			 cookies[i] > 0 and cookies[j] > 0):
			cookie_pairs_count = cookie_pairs_count + 1
			cookies[i] = 0
			cookies[j] = 0

print(cookie_pairs_count)