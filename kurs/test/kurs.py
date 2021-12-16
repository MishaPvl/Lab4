import random as rnd

def gen_graph(n = 1000, m = 100000):
	graph = open("graph.txt", 'w')
	cycle = open("cycle.txt", 'w')

	graph.write(str(n) + ' ' + str(m) + "\n")

	count = (m // n) - 1
	if count == 0:
		count = 1
	print(count)
	for i in range(n - 1):
		if i != n - 1:
			cycle.write(str(i + 1) + ' ')
	for i in range(n):
		for j in range(count):
			v = rnd.randint(1, n - 1)
			while v == i:
				v = rnd.randint(1, n - 1)
			graph.write(str(i+1) + ' ' + str(v) + "\n")

	graph.write(str(n) + ' ' + str(1))
	cycle.write(str(n))

	graph.close()
	cycle.close()

gen_graph()