# Author: Noah Frawley
# Description: RPS for my checkpoint project on codedex.io "The Legend of Python" course!

import random

playing = True
options = [
    '✊',
    '✋',
    '✌️',
]

while playing:
    # Print game menu
    print('======================================')
    print('== Rock Paper Scissors Lizard Spock ==')
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
        exit

    # Roll CPU's choice
    cpu = options[random.randint(0,2)]

    # Display choices
    print()
    print('You chose: ' (user))
    print('CPU chose: ' (cpu))
    print()
    print('======================================')

    # Loop back to choices if they want to continue
    continue_choice = str(input('Would you like to continue (Y/N)?'))
    if continue_choice.upper() == 'Y':
        playing = True
    else:
        playing = False