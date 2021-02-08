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

failed = False
for attempts in range(0,3):
    pwd = input('Type in your password: ')
    if pwd == password:
        break
    elif attempts == 2:
        attempts += attempts
        failed = True
        break
    else:
        print('Nope.')
        
if failed == False:
    print('Access granted. Failed attempts: '+ str(attempts))
else:
    print('You forgot your password.')
