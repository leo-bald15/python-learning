def spam(): #this program will print out 99; eggs variable is destroyed once bacon() returns
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
