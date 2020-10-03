#program based on PyCon 2015 talk by Nez Batchelder; Python names and values
def multiplyByTen(a_list, i):
    a_list[i] = a_list[i] * 10
    return a_list

nums = [1,2,3]
print('The list nums contains: ' + str(nums))
for x  in range(len(nums)):
    newList = multiplyByTen(nums, x)
    nums = newList
    print('Muliplying index ' + str(x) + ' in list "nums" by ten')
    print(nums)

print()

diez = [10,20,30]
for i in range(len(diez)):
    other = multiplyByTen(diez, i)
    diez = other
    print('Muliplying index ' + str(i) + ' in list "diez" by ten')
    print(diez)
