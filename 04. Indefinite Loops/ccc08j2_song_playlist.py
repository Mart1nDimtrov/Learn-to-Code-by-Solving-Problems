# DMOJ problem ccc08j2, Song Playlist

stop = 0
songs = ["A", "B", "C", "D", "E"]

while True:
	button1 = int(input())
	button2 = int(input())

	if button1 == 4 and button2 == 1:
		break

	for i in range(button2):
		if button1 == 1:
			first = songs.pop(0)
			songs.append(first)
		elif button1 == 2:
			last = songs.pop()
			songs.insert(0, last)
		elif button1 == 3:
			temp = songs[0]
			songs[0] = songs[1]
			songs[1] = temp

print(" ".join([song for song in songs]))