import random as rnd

def check_errors(n, m):
	if n > 1000:
		print("n должно быть <= 1000.")
		exit()
	if m > n**2:
		print("m должно быть <= n^2")
		exit()

def check_cycle(matrix, cycle, n):
	if len(set(cycle)) != n:
		print("Неправильный гамильтонов цикл.")
		return False
	for i in range(n - 1):
		if cycle[i + 1] not in matrix[cycle[i] - 1]:
			print(cycle[i + 1], matrix[cycle[i] - 1])
			print("Неправильный гамильтонов цикл.")
			return False

	print("Гамильтонов цикл правильный")
	return True

def get_p_matrix(matrix, cycle, n, cycle_n=1000):
	new_index = [(i + 1) for i in range(n)]
	rnd.shuffle(new_index)

	new_index_file = open("new_index.txt", "w")
	for i in range(n):
		det = ''
		if i != n:
			det = ' '
		new_index_file.write(str(new_index[i]) + det)
	new_index_file.close()

	p_matrix = [set() for i in range(n)]
	p_cycle = []
	for i in range(n):
		for v in range(1, n + 1):
			if v in matrix[i]:
				p_matrix[new_index[i] - 1].add(new_index[v - 1])

		if i < cycle_n:
			p_cycle.append(new_index[cycle[i] - 1])

	return p_matrix, p_cycle

def bob_check_p_matrix(matrix, p_matrix, p_index, n):
	for i in range(n):
		for v in range(1, n + 1):
			if v in p_matrix[i]:
				if (p_index.index(v) + 1) not in matrix[p_index.index(i + 1)]:
					print("Alice обманула.")
					return False

	print("Alice доказала изоморфность графа.")
	return True

def matrix_to_file(filename, w_matrix, n, m):
	p_graph_file = open(filename, 'w')
	p_graph_file.write(str(n) + " " + str(m) + "\n")
	for i in range(n):
		str_v = ''
		for v in w_matrix[i]:
			det = '\n'
			if i == n:
				det = ''
			str_v += str(i + 1) + " " + str(v) + det
		p_graph_file.write(str_v)
	p_graph_file.close()

def cycle_to_file(filename, p_cycle):
	p_cycle_file = open(filename, 'w')
	for v in p_cycle:
		p_cycle_file.write(str(v) + " ")
	p_cycle_file.close()


def gen_graph(n = 1000, m = 100000):
	file = open("graph.txt", 'w')
	cycle = open("cycle.txt", 'w')

	file.write(str(n) + ' ' + str(m) + "\n")

	count = (m // n) - 1
	if count == 0:
		count = 1

	for i in range(n - 1):
		file.write(str(i + 1) + ' ' + str(i + 2) + "\n")
		if i != n - 1:
			cycle.write(str(i + 1) + ' ')
	for i in range(n):
		for j in range(count):
			v = rnd.randint(1, n - 1)
			while v == i:
				v = rnd.randint(1, n - 1)
			file.write(str(i+1) + ' ' + str(v) + "\n")

	file.write(str(n) + ' ' + str(1))
	cycle.write(str(n))

	file.close()
	cycle.close()

def file_len(filename="graph.txt"):
	with open(filename) as f:
		return sum(1 for _ in f)

def get_matrix(filename = "graph.txt"):
	file = open(filename, 'r')

	n, m  = file.readline().split(' ')

	matrix = [set() for i in range(int(n))]

	line = file.readline()
	while line:
		v1, v2 = line.split(' ')
		matrix[int(v1) - 1].add(int(v2))
		line = file.readline()
	file.close()
	return matrix, int(n), file_len(filename) - 1

def get_cycle(n = 1000, filename = "cycle.txt"):
	cycle_file = open(filename, 'r')
	cycle = cycle_file.readline().split(' ')
	for i in range(n):
		if cycle[i] == '':
			break
		cycle[i] = int(cycle[i])
	cycle_file.close()
	return cycle

# START
gen_graph()
cycle = get_cycle()
matrix, n, m = get_matrix()
check_errors(n, m)
print('Абонент - Alice, Проверяющий - Bob')
count = int(input('Введите число итераций: '))
print("Проверка будет выполнена на", count, "итерациях:")

for i in range(count):
	p_matrix, p_cycle = get_p_matrix(matrix, cycle, n)
	p_matrix_filename = "p_graph.txt"
	matrix_to_file(p_matrix_filename, p_matrix, n, m)
	p_index_filename = "new_index.txt"
	bob_choise = rnd.randint(0, 1)
	print('-'*50)
	print(f'Bob выбирает {bob_choise}')
	p_index = get_cycle(n, p_index_filename)
	if bob_choise:
		print('-'*50)
		print("Bob просит доказать изоморфность графа.")
		if not bob_check_p_matrix(matrix, p_matrix, p_index, n):
			exit()
		continue
	print('-'*50)	
	print("Bob просит Alice показать гамильтонов цикл.")
	p_cycle_filename = "p_cycle.txt"
	cycle_to_file(p_cycle_filename, p_cycle)

	check = check_cycle(p_matrix, p_cycle, n)
	if not check:
		print("Неправильный путь.")
		exit()

print("Вероятность обмана: ", 1 / (2 ** count))

wrong_cycle_n = 999
wrong_cycle = get_cycle(wrong_cycle_n, "wrong_cycle.txt")
print('-'*50)
print("Поступление неправильного гамильтонова цикла:")
p_matrix, p_cycle = get_p_matrix(matrix, wrong_cycle, n, wrong_cycle_n)

p_matrix_filename = "p_graph.txt"
matrix_to_file(p_matrix_filename, p_matrix, n, m)

print("Боб просит Алису показать гамильтонов цикл.")
p_cycle_filename = "p_cycle.txt"
cycle_to_file(p_cycle_filename, p_cycle)

check_cycle(p_matrix, p_cycle, n)
print('-'*50)
print("Поступление неправильного изоморфного графа:")
p_matrix_filename = "wrong_graph.txt"
p_matrix, n, m = get_matrix(p_matrix_filename)

p_index_filename = "new_index.txt"
p_index = get_cycle(n, p_index_filename)
print("Боб просит Алису доказать изоморфность графа.")
bob_check_p_matrix(matrix, p_matrix, p_index, n)
