#type() tells you the data type
myDict = {
    'name':'Leo',
    'age':17,
    'ethnicity':'hispanic'
    }

print(type(42)) #int
print(type('hello')) #str
print(type(3.14)) #float
print(type(myDict)) #dict
print(type(True)) #bool
print()
if type(42) == int:
    print('this is an int')
else:
    print('idk what 42 is but it aint an int')

try:
    inp = int(input('type in a number please: '))
    if type(inp) == int:
        print('thanks')
except ValueError:
    print('that is not a number')
