# DMOJ problem sac22cc5jp2, Badminton Scoring

games = int(input())
games_won = 0

for i in range(games):
	game_input = input().split()
	score_1 = int(game_input[0])
	score_2 = int(game_input[1])

	if score_1 > score_2:
		games_won = games_won + 1

print(games_won)
