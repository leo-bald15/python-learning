#built-in methods for lists

#.append() adds a new value to the end of the list

#.insert() adds a new value according to the index specified; moves following values up

'''
spam = ['cat', 'dog', 'rat', 'mat']
print(spam)

print('appending to spam...')

spam.append('hat')
print(spam)

eggs = ['bell', 'tell','fell']
print(eggs)

print(r'inserting to "eggs" ' )
eggs.insert(2, 'hell')
print(eggs)

'''
print('This program will create a list for you.')
print('Would you like to create a list?')
print('Type y for Yes or n for No')
answer = input()

if answer == 'y':
    print('what would you like to name your list?')
    listname = input()
    print('list created!')
    creation = []

    for i in range(10):
        print('What would you like to add?')
        print('Maximum of 10 items')
        addition = input()

        creation.append(addition)
        print('Item added!')
    else:
        print('program ended')
print(listname + ': ' + str(creation))















