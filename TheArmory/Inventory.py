#   Inventory shall consist of:
#       - Unique Currency
#       - Equipped Primary Weapon
#       - Holstered Secondary Weapon
#       - First Aid Consumables

def weapon_selection():
    primary = 0
    str_primary = 'None'
    secondary = 0
    str_secondary = 'None'
    while True:
        print("----------------------------------------------------------------------")
        print("""
 __      __                         ___      _        _   _          
 \ \    / /__ __ _ _ __  ___ _ _   / __| ___| |___ __| |_(_)___ _ _  
  \ \/\/ / -_) _` | '_ \/ _ \ ' \  \__ \/ -_) / -_) _|  _| / _ \ ' \ 
   \_/\_/\___\__,_| .__/\___/_||_| |___/\___|_\___\__|\__|_\___/_||_|
                  |_|                                                
        """)
        print("----------------------------------------------------------------------")
        print('')
        print('Select primary weapon:\n\t0. Fist\n\t1. Knife\n\t2. Handgun\n')
        while True:
            primary = int(input('Selection:\t'))
            if primary not in range(3):
                print('Invalid Input\n')
                continue
            elif primary in range(3):
                break
        str_primary = primary_weapons[primary]
        print('\nYou have selected ' + str_primary)
        confirmation = int(input('\nAre you sure?\n1. Yes\n2. No\n'))
        if confirmation == 1:
            print('Current equipped primary is: ' + str_primary)
            break
        elif confirmation == 2:
            continue
        else:
            print('Invalid input!')
            continue
    while True:
        print("----------------------------------------------------------------------")
        print('')
        print('Select secondary weapon:\n\t0. Fist\n\t1. Knife\n\t2. Handgun\n')
        while True:
            secondary = int(input('Selection:\t'))
            if secondary == primary:
                print('Weapon already selected as primary! Select a different weapon')
                continue
            str_secondary = primary_weapons[secondary]
            print('\nYou have selected ' + str_secondary)
            confirmation = int(input('\nAre you sure?\n1. Yes\n2. No\n'))
            if confirmation == 1:
                print('Current equipped secondary is: ' + str_secondary)
                break
            elif confirmation != 2:
                print('Invalid input!')
        return primary,secondary


def inventory():
    print("----------------------------------------------------------------------")
    print("""
 _____                     _                   
|_   _|                   | |                  
  | | _ ____   _____ _ __ | |_ ___  _ __ _   _ 
  | || '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
 _| || | | \ V /  __/ | | | || (_) | |  | |_| |
 \___/_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
                                          __/ |
                                         |___/ 
    """)
    print("----------------------------------------------------------------------")



primary_weapons = ['Fist', 'Knife', 'Handgun']
inven=[]
w1,w2=weapon_selection()
print(w1,w2)
inven.append(w1)
inven.append(w2)
print(inven)
print('Active primary weapon: \n' ,primary_weapons[inven[0]])
print('Active secondary weapon: \n' + primary_weapons[inven[1]])