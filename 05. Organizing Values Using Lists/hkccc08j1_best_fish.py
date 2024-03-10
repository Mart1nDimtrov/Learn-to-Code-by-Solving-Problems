# DMOJ problem hkccc08j1, Best fish

casper_fish_count = int(input())
casper_fishes = []

for i in range(casper_fish_count):
	fish_input = input().split()
	fish_weight = int(fish_input[0])
	fish_length = int(fish_input[1])
	casper_fishes.append(fish_weight * fish_length)

natalie_fish_count = int(input())
natalie_fishes = []

for i in range(natalie_fish_count):
	fish_input = input().split()
	fish_weight = int(fish_input[0])
	fish_length = int(fish_input[1])
	natalie_fishes.append(fish_weight * fish_length)

if max(natalie_fishes) > max(casper_fishes):
	print("Natalie")
elif max(natalie_fishes) < max(casper_fishes):
	print("Casper")
else:
	print("Tie")