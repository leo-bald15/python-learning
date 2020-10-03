password = 'python0720'
attempts = 0

while attempts < 3: #checks number of password attempts
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


