verify_ans = 0

def login():
    username = 'none'
    password = 'none'
    counter = 5

    while username != 'Admin' or password != 'password':
        print('-----------------------------')
        print('\nLogin Page')
        print('Tries left:\t',{counter})
        username = str(input('Username:\t'))
        password = str(input('Password:\t'))

        usnFlag = 'Admin' == username
        pasFlag = 'password' != password

        if usnFlag and not pasFlag:
            return mainmenu()

        elif usnFlag:
            counter -= 1
            print('Password Incorrect')

        elif not pasFlag:
            counter -= 1
            print('Credentials Incorrect')
        elif counter == 0:
            return shutdown()

        else:
            counter -= 1
            print('User does note exist')



def mainmenu():
    print('-----------------------------')
    print('\n Main Menu')
    termination = str(input('Press any key to exit'))

def shutdown():
    print('-----------------------------')
    print('\nGoodbye')
    exitmessage = str(input('Press any key to exit'))

def confirmation():
    print('-----------------------------')
    print('\n Are you sure?\n0. Yes\n1. No')
    verify = int(input('Selection:\t'))
    verify_ans = verify
    return

def confirmation_test(verify_ans):
    print('-----------------------------')
    print('\nHello')
    return confirmation()
    print(verify_ans)

print(confirmation_test())