# 7.DMOJ problem coci18c4p1, Elder

current_winner = input()
number_of_duels = int(input())
wizard_count = 1
all_winners =  current_winner

for duel in range(number_of_duels):
	wizards_in_duel = list(input().split(" "))
	wizard_won = wizards_in_duel[0]
	wizard_lost = wizards_in_duel[1]
	if wizard_lost == current_winner:
		current_winner = wizard_won
		if current_winner not in all_winners:
			all_winners = all_winners + current_winner
			wizard_count = wizard_count + 1

print(current_winner)
print(wizard_count)