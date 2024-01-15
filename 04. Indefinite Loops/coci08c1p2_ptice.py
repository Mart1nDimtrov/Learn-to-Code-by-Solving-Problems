# 2.DMOJ problem coci08c1p2, Ptice

length = int(input())
answers = input()
bird_lovers = {
	"adrian" : 0,
	"bruno" : 0,
	"goran" : 0
}

for i in range(length):
	if ((i % 3 == 0 and answers[i] == "A") or
		(i % 3 == 1 and answers[i] == "B") or
		(i % 3 == 2 and answers[i] == "C")):
		bird_lovers["adrian"] = bird_lovers["adrian"] + 1
	if ((i % 4 == 0 and answers[i] == "B") or
		(i % 4 == 1 and answers[i] == "A") or
		(i % 4 == 2 and answers[i] == "B") or
		(i % 4 == 3 and answers[i] == "C")):
		bird_lovers["bruno"] = bird_lovers["bruno"] + 1
	if ((i % 6 == 0 and answers[i] == "C") or
		(i % 6 == 1 and answers[i] == "C") or
		(i % 6 == 2 and answers[i] == "A") or
		(i % 6 == 3 and answers[i] == "A") or
		(i % 6 == 4 and answers[i] == "B") or
		(i % 6 == 5 and answers[i] == "B")
		):
		bird_lovers["goran"] = bird_lovers["goran"] + 1


max_value = max(bird_lovers.values())
print(max(bird_lovers.values()))
[print(k.title()) for k, v in bird_lovers.items() if v == max_value]