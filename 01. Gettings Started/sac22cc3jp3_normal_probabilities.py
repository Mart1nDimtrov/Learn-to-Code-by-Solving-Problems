# DMOJ problem sac22cc3jp3, Normal Probabilities

probabilities = {
	"A":1.0,
	"B":0.8,
	"C":0.6,
	"D":0.4,
	"E":0.2
}

n = int(input())
sum_of_probabilities = 1.0

for i in range(n):
	sum_of_probabilities = sum_of_probabilities * probabilities[input()]

print(sum_of_probabilities)