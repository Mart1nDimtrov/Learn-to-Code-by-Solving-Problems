# USACO 2018 December Bronze Contest problem Mixing Milk
def get_a_and_b(c_a, m_a, c_b, m_b):
	"""Return the proper amounts for a and b"""
	amount = 0
	if c_b != m_b:
		if m_a + m_b >= c_b:
			amount = c_b - m_b
			m_b = c_b
			m_a = m_a - amount
		elif m_a + m_b < c_b:
			amount = m_a + m_b
			m_b = amount
			m_a = 0
	else:
		m_a = m_a
		m_b = m_b

	return m_a, m_b

input_file = open('mixmilk.in', 'r')
output_file = open('mixmilk.out', 'w')

b_m = []
line = input_file.readline().split()
while line != []:
	b_m.append([int(line[0]), int(line[1])])
	line = input_file.readline().split()

for i in range(0, 100):
	if i % 3 == 2:
		milk_a = b_m[2][1]
		capacity_a = b_m[2][0]
		milk_b = b_m[0][1]
		capacity_b = b_m[0][0]
		milk_a_new, milk_b_new = get_a_and_b(capacity_a, milk_a, capacity_b, milk_b)
		b_m[2][1] = milk_a_new
		b_m[0][1] = milk_b_new
	elif i % 3 == 0:
		milk_a = b_m[0][1]
		capacity_a = b_m[0][0]
		milk_b = b_m[1][1]
		capacity_b = b_m[1][0]
		milk_a_new, milk_b_new = get_a_and_b(capacity_a, milk_a, capacity_b, milk_b)
		b_m[0][1] = milk_a_new
		b_m[1][1] = milk_b_new
	elif i % 3 == 1:
		milk_a = b_m[1][1]
		capacity_a = b_m[1][0]
		milk_b = b_m[2][1]
		capacity_b = b_m[2][0]
		milk_a_new, milk_b_new = get_a_and_b(capacity_a, milk_a, capacity_b, milk_b)
		b_m[1][1] = milk_a_new
		b_m[2][1] = milk_b_new

for i, v in b_m:
	print(v)