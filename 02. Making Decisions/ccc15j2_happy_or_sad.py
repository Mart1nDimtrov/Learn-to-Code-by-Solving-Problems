# 3.DMOJ problem ccc15j2, Happy or Sad

message = input()
happy_count = message.count(":-)")
sad_count = message.count(":-(")

if happy_count > sad_count:
	print("happy")
elif happy_count < sad_count:
	print("sad")
elif happy_count == sad_count and sad_count != 0:
	print("unsure")
else:
	print("none")