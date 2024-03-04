**Pyramid**
- First I imported the code example from class as a reminder of how to make the pyramid formation.
- I changed the code from "if j >= i:" to "if j <= i:" which flipped the pyramid vertically, but i still need it to angle to the right instead of left.
- Stepped backwards and made the variable "stacks" and wrote the prompt "stacks = int(input("How tall would you like the pyramid to be?"))"
- Wanted to put the pyramid code into "if stacks == 1: print (1)", but there seems to be a syntax error. Can you not do code within code?
- Instead of coding each stack of pyramid individually I changed the the range to be "stacks+1" and "i +1"
Still need to flip the pyramid and get the correct number of #.
This website helped me understand why my # were starting on 2 instead of 1. I needed to make my code "for j in range (1,i+1" when before I had it as "for j in ranfe (i+1)" This makes it possible for the pattern to start in the right place which is 1. (https://www.programiz.com/python-programming/examples/pyramid-patterns#code3)
Tried to write "else: stacks > 8 or stacks < 1
print("Number not in range.")" But when I run it the pyramid still appears. Trying to adjust my range, but it is also affecting the pyramid.
Tried playing around with nesting the code within the original and using " " to complete the square like we discussed, but having trouble. 
