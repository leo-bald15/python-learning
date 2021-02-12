#this program will detect a palindrome
def palindrome(list_one, list_two): #only accepts list values, compares them
   try:
      if list_one == list_two:
         return True #it is a palindrome
      else:
         return False #it is not a palindrome
   except:
         return

print('Type in a word and I will tell you if its a palindrome')
while True:
   prompt = input('Input: ')
   #creating first argument
   firstList = list(prompt)
   #creating second argument
   secondList = []
   for i in range(len(firstList) -1,-1, -1):
      secondList.append(firstList[i])

   #calling function with parameters
   result = palindrome(firstList, secondList)
   if result == True:
      print('It is a palindrome. Have another word in mind?')
      continue
   elif result == False:
      print('It is not a palindrome. Have another word in mind?')
      continue
   else:
      print('Invalid input. Please type in a word')