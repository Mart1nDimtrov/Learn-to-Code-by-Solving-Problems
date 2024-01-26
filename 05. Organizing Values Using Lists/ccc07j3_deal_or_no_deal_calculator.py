# 1.DMOJ problem ccc07j3, Deal or No Deal Calculator

boxes = [100, 500, 1000, 5000, 10000, 25000,
		50000, 100000, 500000, 1000000]

open_boxes = int(input())
indexes = []

for i in range(open_boxes):
	box_index = int(input())
	boxes[box_index-1] = 0

offer = int(input())

if offer > (sum(boxes) / (len(boxes) - open_boxes)):
	print("deal")
else:
	print("no deal")


