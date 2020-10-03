#for loops actually iterates through the values of a list
#range returns a list-like value; for an acual list value pass range() to list()

range(4) # will return [0,4]

list(range(4)) # will return [0,1,2,3]

print('first loop')
for i in range(4): #returns 0, 1, 2, 3
    print(i)

print('second loop')
spam = [0,1,2,3]
for i in spam: #returns 0, 1, 2, 3
    print(i)

#variables can have multiple assignment statements on one line

cat = ['Pooka' ,'orange','timid']
name, color, personality = cat

print(name, color, personality)

#example 2
nombre, age, heightcm = 'leo', 17, 179

print(nombre, age, str(heightcm) + 'cm')
