name = input('Set name: ')
password = input('Set password: ')
while 1 == 1:
    nameguess=""
    passwordguess=""
    key=""
    while (nameguess != name) or (passwordguess != password):
        nameguess = input('Name? ')
        passwordguess = input('password? ')
    print("Welcome,",name, ". Type lock to lock.")
    while key != "lock":
        key = input("")
