# DMOJ problem mwc15c1p1, Playlist Panic

n_songs = int(input())
songs = []

for i in range(n_songs):
	new_song_input = input().split()
	# turn song time to seconds
	songs.append((int(new_song_input[0]) * 60) + int(new_song_input[1]))

time_available_input = input().split()
time_available = (int(time_available_input[0]) * 60) + int(time_available_input[1])
# sort song from smallest
songs.sort()

sum_of_songs = 0
count_of_songs = 0
for i_2 in range(n_songs):
	if (sum_of_songs + songs[i_2]) > time_available:
		break
	else:
		sum_of_songs = sum_of_songs + songs[i_2]
		count_of_songs = count_of_songs  + 1

print(count_of_songs)