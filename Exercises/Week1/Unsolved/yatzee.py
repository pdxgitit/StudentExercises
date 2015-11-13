import random

dice = {
    '1': ('   ', ' o ', '   '),
    '2': ('o  ', '   ', '  o'),
    '3': ('o  ', ' o ', '  o'),
    '4': ('o o', '   ', 'o o'),
    '5': ('o o', ' o ', 'o o'),
    '6': ('o o', 'o o', 'o o')
}

score_card = {
    "Aces": 0,
    "Twos": 0,
    "Threes": 0,
    "Fours": 0,
    "Fives": 0,
    "Sixes": 0,
    "Bonus": 0,
    "3ofKind": 0,
    "4ofKind": 0,
    "FullHouse": 0,
    "SmallStraight": 0,
    "LargeStraight": 0,
    "Yahtzee": [0, 0, 0]
}

t_or_b = '-----'
side = '|'
choices = ['1', '2', '3', '4', '5']
new_choices = []
new_rolls = []

def roller(num):
    rolls = []
    for i in range(num):
        rolls.append(str(random.randint(1,6)))
    return rolls


def print_dice(roll_list):
    print ((t_or_b + " ") * len(roll_list))
    for i in range(3):
        line = ''
        for num in roll_list:
            line += side + dice[num][i] + side + ' '
        print (line)
    print ((t_or_b + " ") * len(roll_list))


def print_choice(choice_list):
    space = ' ' * 5
    print ('  ' + space.join(choice_list))


def printer(roll_list, choice_list, num):
    print("\n" * 100)
    print_dice(roll_list)
    print_choice(choice_list)
    print("It is roll {}".format(num + 1))


def hold_die(roll_list, choice_list, num):
    while True:
        try:
            choice = input('Enter number to hold - type D to roll: ')
            print(choice)
            if choice == 'D':
                return choice_list
            elif len(choice) > 1 or choice not in '12345':
                raise ValueError()
            elif len(choice) == 1 and choice_list[int(choice) - 1] == 'X':
                choice_list[int(choice) - 1] = str(int(choice))
                printer(roll_list, choice_list)
            else:
                choice_list[int(choice) - 1] = 'X'
                printer(roll_list, choice_list, num)
        except ValueError:
            print ("Invalid input")


def count_holds(roll_list):
     return 5 - roll_list.count('X')


def merge_dice(choice_list, new_rolls, last_rolls):
    ndx = 0
    for val in choice_list:
        if val != 'X':
            last_rolls[choice_list.index(val)] = new_rolls[ndx]
            ndx += 1
    return last_rolls


roll_1 = roller(5)

for turn in range(3):
    roll_2 = merge_dice(new_choices, new_rolls, roll_1)
    printer(roll_1, choices, turn)
    new_choices = hold_die(roll_1, choices, turn)
    roll_again = count_holds(new_choices)
    if roll_again == 0 or turn == 2:
        break
    new_rolls = roller(roll_again)
    
print(roll_2)
