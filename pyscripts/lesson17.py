#dictionaries are made with curly braces
#dictionaries are a mutable data type

myCat = {
    'size':'fat'
    'color':'gray'
    'disposition':'loud'
    }
print('my cat ' + myCat['color'] + ' fur.')

#dictionaries can have numbers as keys
spam = {
    12345:'Luggage Combination', '42':'The Answer'
    }

#order in lists matter whilst dictionaries do not take that into account
a_list = [1,2,3]
anotherList = [3,2,1]
print(a_list == anotherList) #False

a_dict = {
    'name':'Zophie',
    'species':'cat',
    'age':8
}
another_dict = {
    'species':'cat',
    'age':8,
    'name':'Zophie'
    }
print(a_dict == another_dict) #True

print('name' in a_dict) #true
print('name' not in another_dict) #False

#dictionary methods

#.keys()
list(a_dict.keys()) # ['name', 'species', 'age']
#.values()
list(a_dict.values()) # ['Zophie', 'cat', 8]
#.items()
list(a_dict.items()) # [('name':'Zophie') , ('species':'cat'), ('age':8)]


#no need to convert the dictionary to list-like values
for v in a_dict.values():
    print(v)
print()
for k,v in a_dict.items():
    print(k,v)
