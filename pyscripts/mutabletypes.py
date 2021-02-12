import copy #can create a new list, not a refer
def eggs(cheese):
   cheese = copy.deepcopy(spam)
   #deepcopy will create a clone of the og list
   cheese.append('change')
   return cheese
   
spam = [1,2,3]
print(eggs(spam)) #[1,2,3,'change']
print(spam) #[1,2,3]
