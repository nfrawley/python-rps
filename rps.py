# Author: Noah Frawley
# Description: RPS for my checkpoint project on codedex.io "The Legend of Python" course!

import random

playing = True
options = [
    '✊',
    '✋',
    '✌️',
]
cpu_wins = 0
user_wins = 0

while playing:
    # Print game menu
    print('======================================')
    print('======== Rock Paper Scissors =========')
    print('======================================')
    print('Options:')
    print('1) ✊')
    print('2) ✋')
    print('3) ✌️')
    print('======================================')
    
    # Capture user choice, check it's in correct range of options, convert to array value (0 indexed)
    user_choice = int(input('Please choose (1-3):'))
    if 0 < user_choice <= 3:
        user = options[user_choice - 1]
    else:
        print('Try again, dummy!')
        continue

    # Roll CPU's choice
    cpu = options[random.randint(0,2)]

    # Compare to determine winner
    if user == '✊':
        if cpu == '✊':
            winning_player = "Nobody"
        elif cpu == '✋':
            winning_player = "CPU"
            cpu_wins += 1
        elif cpu == '✌️':
            winning_player = "User"
            user_wins += 1
    elif user == '✋':
        if cpu == '✊':
            winning_player = "User"
            user_wins += 1
        elif cpu == '✋':
            winning_player = "Nobody"
        elif cpu == '✌️':
            winning_player = "CPU"
            cpu_wins += 1
    elif user == '✌️':
        if cpu == '✊':
            winning_player = "CPU"
            cpu_wins += 1
        elif cpu == '✋':
            winning_player = "User"
            user_wins += 1
        elif cpu == '✌️':
            winning_player = "Nobody"

    # Display choices
    print()
    print('You chose:', user)
    print('CPU chose:', cpu)
    print(f'{winning_player} wins this round!')
    print('======================================')
    print('User wins:', user_wins)
    print('CPU wins:', cpu_wins)
    print('======================================')

    # Loop back to choices if they want to continue
    continue_choice = str(input('Would you like to continue (Y/N)?'))
    if continue_choice.upper() == 'Y':
        playing = True
    else:
        playing = False
