# DMOJ problem ccc99s1, Card Game

def check_result(position, card, deck):
	result = 0
	cards_length = 52
	high_cards_arr = ["ace", "king", "queen", "jack"]

	if card == "ace" and (cards_length - 5) >= position and not (x for x in deck[position+1:position+5] if x in high_cards_arr):
		result = 4
	elif card == "king" and (cards_length - 4) >= position and not (x for x in deck[position+1:position+4] if x in high_cards_arr):
		result = 3
	elif card == "queen" and (cards_length - 3) >= position and not (x for x in deck[position+1:position+3] if x in high_cards_arr):
		result = 2
	elif card == "jack" and (cards_length - 2) >= position and not (x for x in deck[position+1:position+2] if x in high_cards_arr):
		result = 1

	return result

deck = []
player_a_points = 0
player_b_points = 0

for i in range(52):
	card = deck.append(input())

for i_2 in range(52):
	if i_2 % 2 == 0:
		player_a_points = player_a_points + check_result(position=i_2, card=deck[i_2], deck=deck)
	elif i_2 % 2 == 1:
		player_b_points = player_b_points + check_result(position=i_2, card=deck[i_2], deck=deck)
	print(check_result(position=i_2, card=deck[i_2], deck=deck))

print(player_a_points)
print(player_b_points)
	

