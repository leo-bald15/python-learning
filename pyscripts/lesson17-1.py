#.get() method
myDict = {
    'name':'Leo',
    'age': 17,
    'species': 'human'
    }
if 'age' in myDict:
    print(myDict['age'])
else:
    print('There is no key with that name')

#shortened down to this 
print(myDict.get('age', 'There is no key with that name'))

#.setdefault() same as .get() but will automaticaly create the value
if 'eyeC' not in myDict:
    myDict['eyeC'] = 'brown'

myDict = { #reseting dictionary for example use
    'name':'Leo',
    'age': 17,
    'species': 'human'
    }
#shortened down to this
myDict.setdefault('eyeC', 'brown')
