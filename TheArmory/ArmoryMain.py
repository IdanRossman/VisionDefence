#   Welcome to the Armory!
#   The following are the goals,requirements and objectives for this program:
#
#   1. Login Screen
#       - User shall enter the Username and Password values
#       - Username : Admin    Password : password
#       - User shall have 5 tries to enter the correct username and password values
#       - Upon 5 failed attempts of either username or password, program shall terminate
#       - If both the credentials entered are incorrect, program shall terminate
#       - Tries remaining for the user to enter the correct credentials shall be displayed
#
#   2. Main Menu
#       - All the optional pages and programs in the system shall be displayed for the user
#       - The user can select which page he would like to access via the selection line
#       - Selecting [0] shall navigate the user to [Armory]
#       - Selecting [1] shall navigate the user to [Firing Range]
#       - Selecting [2] shall navigate the user to [Login Page]
#       - Selecting [3] shutdown the program
#
#
#   3. Weapon selection
#       - This will include informing the user of the current available weapons
#       - Verification of user selection
#       - General Information about the current selected weapon such as magazine size,
#         bullet caliber and ballistic recommendations
#
#   4. Weapon Ballistics
#       - Each weapon shall have range multipliers for damage, for example: a shotgun
#         fired from close range shall carry more impact then in longer ranges.
#       - Each weapon shall have it's ballistic information for ranges, kill zones.
#
#   5. Dummy Target and Hit probability
#       - For now the weapons shall be fired in the "Firing Range"
#       - The 'Firing Range' shall have a range of a maximum of 200m
#       - 'Dummies' or 'Targets' can be placed in all ranges from a minimum of 10m to
#         to a maximum of 100m
#       - Fire probability and hit percentage shall include ballistic calculations and
#         shall include a RNG element.


#   login screen shall include input of both username and password
#   Only in the case where both the username and password match, shall the user be
#   permitted to carry on.


def login():
    print('___________________________________________________________________________________________________')
    print("""
 ___      _______  _______  ___   __    _ 
|   |    |       ||       ||   | |  |  | |
|   |    |   _   ||    ___||   | |   |_| |
|   |    |  | |  ||   | __ |   | |       |
|   |___ |  |_|  ||   ||  ||   | |  _    |
|       ||       ||   |_| ||   | | | |   |
|_______||_______||_______||___| |_|  |__|
    """)
    print('Vision Defence Protocols')
    print('LOGIN SCREEN')

    username = 'none'
    password = 'none'
    tries = 5

    while 'Admin' != username or 'password' != password:

        print("")
        print('Tries Left: ' + str(tries))
        username = str(input('Username '))
        password = str(input('Password '))

        if 'Admin' == username and 'password' == password:
            return mainmenu()

        #           All GOOD - Move to weapon selection
    usrFlag= 'Admin' == username
    psdFlag="password" != password

    if not usrFlag:
        a=1
    elif not psdFlag:
        b=1
    else:
        c=1

        if 'Admin' == username and 'password' != password:
            print('Password Incorrect!')
            tries -= 1
            if tries == 0:
                return termination()
        #           Password incorrect
        #           Return to beginning login screen to re-enter credentials

        if 'Admin' != username and 'password' == password:
            print('Credentials Incorrect!')
            tries -= 1
            if tries == 0:
                return termination()
        #           User name incorrect
        #           Return to beginning login screen to re-enter credentials

        if 'Admin' != username and 'password' != password:
            return termination()
    #               Both Incorrect - SHUTDOWN

def termination():
    print('___________________________________________________________________________________________________')
    print("")
    print("SECURITY BREACH!\nSystem Termination in progress")

def shutdown():
    print('___________________________________________________________________________________________________')
    print('')
    print("Goodbye")
#


def mainmenu():
    print('___________________________________________________________________________________________________')
    print("""
  __  __         _          __  __                     
 |  \/  |       (_)        |  \/  |                    
 | \  / |  __ _  _  _ __   | \  / |  ___  _ __   _   _ 
 | |\/| | / _` || || '_ \  | |\/| | / _ \| '_ \ | | | |
 | |  | || (_| || || | | | | |  | ||  __/| | | || |_| |
 |_|  |_| \__,_||_||_| |_| |_|  |_| \___||_| |_| \__,_|                                           
    """)
    print('')
    print('Access Granted!\nWelcome Back Sir.')

    #   0. Armory
    #   1. Firing Range
    #   2. Return to Login Screen
    #   3. Exit Program

    print("")
    print('What would you like to do?')
    print('0. Armory\n1. Firing Range\n2. Return to Login Screen\n3. Exit Program')
    print("")
    selection = int(input('Selection: '))

    if selection == 0:
        print('')
        print('Currently Unavailable')
        return mainmenu()

    elif selection == 1:
        print('')
        print('Currently Unavailable')
        return mainmenu()

    elif selection == 2:
        return login()

    elif selection == 3:
        return shutdown()

    else:
        print('')
        print('Selection Not Valid, Try Again!')
        return mainmenu()


print(login())









