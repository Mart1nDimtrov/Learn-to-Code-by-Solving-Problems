# DMOJ problem coci17c1p1, Cezar

all_cards = [2, 3, 4, 5, 6, 7,
			 8, 9, 10, 10, 10, 10, 11]
all_cards = all_cards * 4
my_cards = 0

n_drawn_cards = int(input())

for i in range(n_drawn_cards):
	card = int(input())
	my_cards = my_cards + card
	all_cards.remove(card)

diff = 21 - my_cards
bigger = len([x for x in all_cards if x > diff])
smaller = len([x for x in all_cards if x <= diff])

if bigger >= smaller:
	print("DOSTA")
else:
	print("VUCI")