def print_graph(n):
	print('*' * n)

def get_power(x, j):
	return x**j

for i in range(-8, 9):
	print_graph(get_power(i,2))