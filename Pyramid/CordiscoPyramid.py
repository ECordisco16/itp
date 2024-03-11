stacks = int(input("How tall would you like the pyramid to be? Choose a number from 1-8."))
if stacks > 8 or stacks < 1:
    print("Number not in range.") 
elif i in range(0, stacks+1):
  for j in range(1,i+1):
    if j <= i:
      print("#", end='')
  print()
