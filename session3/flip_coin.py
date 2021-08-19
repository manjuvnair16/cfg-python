import random

def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    print('The coin has landed on: {}'.format(side))
    return side

choice = input('heads or tails : ')
result = flip_coin()

if choice == result:
    print('You win')
else:
    print('You lose')