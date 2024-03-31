# DMOJ problem ccc14j2, Vote Count

votes_lenght = int(input())
votes = input()
votes_dict = {}
votes_dict["A"] = 0
votes_dict["B"] = 0

for i in range(votes_lenght):
	votes_dict[votes[i]] = votes_dict[votes[i]] + 1

if votes_dict["A"] > votes_dict["B"]:
	print("A")
elif votes_dict["A"] < votes_dict["B"]:
	print("B")
else:
	print("Tie")


