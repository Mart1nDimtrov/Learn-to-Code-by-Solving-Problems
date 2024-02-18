# DMOJ problem bf1troll, List Minimum (Harder)

n_words = int(input())
positions = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
words = []

for i in range(n_words):
	words.append(input())

words = sorted(words, key = lambda s: [positions.index(x) for x in s if x in positions])
[print(f"{w}", end="\n") for w in words]
