# DMOJ problem a1, Mispelling

n = int(input())
n = n + 1

for i in range(1, n):
	dataset = input().split(" ")
	i_remove = int(dataset[0])
	word = " ".join(dataset[1:])
	word = word[:i_remove-1] + word[i_remove:]
	print(f"{i} {word}")
