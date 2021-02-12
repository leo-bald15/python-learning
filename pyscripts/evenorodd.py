#This programs checks for even or odd numbers

def evenChecker(num):
   try:
      solution = int(num) % 2 #if there is no remainder then, divisible by 2
      if solution == 0:
         return True #even number
      else:
         return False #odd number
   except ValueError:
         return #return value None, error

print("What number are you thinking of?")
while True:
   inp = input("Input a number: ")
   result = evenChecker(inp)
   if result == True:
      print('That\'s an even number. Got another number?')
      continue
   elif result == False:
      print('That\'s an odd number. Got another number?')
      continue
   else:
      print('Invalid Input. Please enter a number.')