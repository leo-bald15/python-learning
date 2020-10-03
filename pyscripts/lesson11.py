def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        return 'Error: You tried to divide by zero', '42/' + str(divideBy)

print(div42by(2))
print(div42by(12))
print(div42by(0))#the try/except statement allows this code to run; dividing by 0
print(div42by(1))
