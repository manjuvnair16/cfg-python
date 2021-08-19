import random

def random_choice():
    choice_number = random.randint(1, 3)

    if choice_number == 1:
        choice = 'r'
    elif choice_number == 2:
        choice = 's'
    else:
        choice = 'p'

    return choice

my_choice = input('Choose rock, scissors or paper - r,s,p : ')
opponent_choice = random_choice()

print('Your opponent chose {}'.format(opponent_choice))

if my_choice == 'r' and opponent_choice == 's':
    print('You win!')
elif my_choice == 'r' and opponent_choice == 'p':
    print('You lose!')
elif my_choice == 's' and opponent_choice == 'r':
    print('You lose!')
elif my_choice == 's' and opponent_choice == 'p':
    print('You win!')
elif my_choice == 'p' and opponent_choice == 'r':
    print('You win!')
elif my_choice == 'p' and opponent_choice == 's':
    print('You lose!')
else:
    print('Its a draw')

