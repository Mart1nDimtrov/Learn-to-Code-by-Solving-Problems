# DMOJ problem ccc99s1, Card Game

def check_result(position, card, deck):
	result = 0
	cards_length = 52
	high_cards_arr = ["ace", "king", "queen", "jack"]

	if card == "ace" and (cards_length - 5) >= position and len([x for x in deck[position+1:position+5] if x in high_cards_arr]) == 0:
		result = 4
	elif card == "king" and (cards_length - 4) >= position and len([x for x in deck[position+1:position+4] if x in high_cards_arr]) == 0:
		result = 3
	elif card == "queen" and (cards_length - 3) >= position and len([x for x in deck[position+1:position+3] if x in high_cards_arr]) == 0:
		result = 2
	elif card == "jack" and (cards_length - 2) >= position and len([x for x in deck[position+1:position+2] if x in high_cards_arr]) == 0:
		result = 1

	return result

deck = []
player_a_points = 0
player_b_points = 0

for i in range(52):
	card = deck.append(input())

for i_2 in range(52):
	points = 0
	if i_2 % 2 == 0:
		points = check_result(position=i_2, card=deck[i_2], deck=deck)
		if points > 0:
			print(f"Player A scores {points} point(s).")
		player_a_points = player_a_points + points
	elif i_2 % 2 == 1:
		points = check_result(position=i_2, card=deck[i_2], deck=deck)
		if points > 0:
			print(f"Player B scores {points} point(s).")
		player_b_points = player_b_points + points

print(f"Player A: {player_a_points} point(s).")
print(f"Player B: {player_b_points} point(s).")
	

