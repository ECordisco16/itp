**Power**
- First I copied the template from the homework
"def print_graph(n):
def get_power(x, n):
for i in range(-8, 9):"
- Then I added this command "print('*', n)" After the print graph command.
  This allowed me to tell the program to print the symbol * "n" number of times.
- I needed to define the function "get_power" for later so I added def get_power(x):
	return x**j
    Not sure if I need to define j?
- Added "for i in range(-8, 9):
	print_graph(get_power(i))""
- Ran it and as expected "j" is not defined.
  Added def get_power(x, j):
    "TypeError: get_power() missing 1 required positional argument: 'j'"
- Took a break and asked a friend who is good with coding and he said I needed to define the "j" by adding "print_graph(get_power(i,2))" at the end of the code.
  Now I think J is defined by "2"?
- This is my code: "def print_graph(n):
	print('*', n)

def get_power(x, j):
	return x**j

for i in range(-8, 9):
	print_graph(get_power(i,2))"
    This is what printed:
* 64
* 49
* 36
* 25
* 16
* 9
* 4
* 1
* 0
* 1
* 4
* 9
* 16
* 25
* 36
* 49
* 64
- Super close- can't quite figure out why its printing the numbers instead of the number of *.
- ohhhh wait- my first command: def print_graph(n):
	print(''*',n) needs to be: print print('*' * n)
- Code printed!
