"""
Write a program that simulates a lottery. The program should have a list of seven numbers that
represent a lottery ticket. It should then generate seven random numbers. After comparing the two
sets of numbers, the program should output a prize based on the number of matches:
● £20 for three matching numbers
● £40 for four matching numbers
● £100 for five matching numbers
● £10000 for six matching numbers
● £1000000 for seven matching numbers
"""

# Lottery ticket will have numbers from 1-59
import random


def generate_winning_tkt_numbers():
    winning_lottery = []
    for var in range(7):
        random_no = random.randint(1, 59)
        winning_lottery.append(random_no)
    return winning_lottery


def count_matching_numbers(my_ticket, winning_tkt):
    count_num_of_matches = 0
    for each_num in my_ticket:
        if each_num in winning_tkt:
            count_num_of_matches += 1
    return count_num_of_matches


PRIZE_RULES_DICT = {
                            3: '£20',
                            4: '£40',
                            5: '£100',
                            6: '£10000',
                            7: '£1000000'
                    }

my_lottery_ticket = [45, 27, 54, 54, 24, 45, 35]
winning_ticket = generate_winning_tkt_numbers()
count_matching_nums = count_matching_numbers(my_lottery_ticket, winning_ticket)
prize_won = PRIZE_RULES_DICT.get(count_matching_nums, '£0')

print('Winning ticket:      {}'.format(winning_ticket))
print('Your lottery ticket: {}'.format(my_lottery_ticket))
print('You have {} matches and you get {}'.format(count_matching_nums, prize_won))
