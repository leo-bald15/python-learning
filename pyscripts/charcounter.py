import pprint
message = 'it was a bright cold day in April, and the clocks were striking thirteen'
count = {} #will contain a key value of each char in message, value of total occurences

for character in message.upper(): #goes through each char
    count.setdefault(character,0)
    count[character] = count[character] + 1
testvar = pprint.pformat(count)#pretty print module
print(testvar)
