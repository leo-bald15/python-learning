password = 'password123'

'''while attempts < 3: #checks number of password attempts
    print("please type in your password")
    psw = input()
    if psw == password: #checks if input matches correct password
        break # breaks loop if password matches
    attempts = attempts + 1 # adds attempt if password is incorrect
    print('wrong password. attempts: ' + str(attempts)) #prints out number of attempts
    #restarts while loop until condition is met or if attempts reach 3


if attempts >= 3: #if attempts are = 3 then quits
    print('Too many failed attempts')
else: #access granted if password matches after while loop ends
    print('Access Granted')
'''

#attempting for loop

for attempts in range(1,4):
    pwd = input('Type in your password: ')
    if pwd == password:
        break
    else:
        print('Nope.')
        
if attempts < 3:
    print('Access granted.')
else:
    print('You forgot your password.')
