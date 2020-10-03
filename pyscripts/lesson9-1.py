def plusOne(number):
    return number + 1


while True:
    num = input('Give me a number and I will add one to it: ' )
    newNumber = plusOne(num)
    print(int(newNumber))
