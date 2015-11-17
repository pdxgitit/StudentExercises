import random

dice = {
    '1': ('   ', ' o ', '   '),
    '2': ('o  ', '   ', '  o'),
    '3': ('o  ', ' o ', '  o'),
    '4': ('o o', '   ', 'o o'),
    '5': ('o o', ' o ', 'o o'),
    '6': ('o o', 'o o', 'o o')
}

score_card = [
    ["Aces", '0'],
    ["Twos", '0'],
    ["Threes", '0'],
    ["Fours", '0'],
    ["Fives", '0'],
    ["Sixes", '0'],
    ["3_of_a_Kind", '0'],
    ["4_of_a_Kind", '0'],
    ["Full_House", '0'],
    ["Small_Straight", '0'],
    ["Large_Straight", '0'],
    ["Chance", '0'],
    ["Yahtzee", '0']
]

t_or_b = '-----'
side = '|'
new_choices = []
new_rolls = []
score = 0

def reset_choices():
    return ['1', '2', '3', '4', '5']

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


def printer(roll_list, choice_list, num, score):
    print("\n" * 100)
    print_dice(roll_list)
    print_choice(choice_list)
    print("It is roll {}".format(num + 1))
    print("Your score is", score)


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
                printer(roll_list, choice_list, num, score)
            else:
                choice_list[int(choice) - 1] = 'X'
                printer(roll_list, choice_list, num, score)
        except ValueError:
            print ("Invalid input")
        finally:


def count_holds(roll_list):
     return 5 - roll_list.count('X')


def merge_dice(choice_list, new_rolls, last_rolls):
    ndx = 0
    for val in choice_list:
        if val != 'X':
            last_rolls[choice_list.index(val)] = new_rolls[ndx]
            ndx += 1
    return last_rolls

def available(score_card):
    while True:
        for ndx, slot in enumerate(score_card):
            if type(slot[1]) == str:
                print("Press {} to store in {}".format(ndx, slot[0]))
        try:
            choice = int(input("Enter number: "))
            if choice not in list(range(13)):
                raise ValueError()
            elif type(score_card[choice][1]) == str:
                return choice
        except ValueError:
            print ("Invalid input")

def convert(string_list):
    num_list = []
    for item in string_list:
        num_list.append(int(item))
    return num_list

def write_score(score_card, roll, ndx):
    roll = convert(roll)
    total = 0
    count = 0
    last = 0
    check = False
    if ndx <= 5: # 6s to Aces
        for val in roll:
            if val == ndx + 1:
                total += val
    elif ndx == 6: # 3 of a kind
        for val in roll:
            total += val
            if roll.count(val) >= 3:
                check = True
        if not check:
            total = 0
    elif ndx == 7: # 4 of a kind
        for val in roll:
            total += val
            if roll.count(val) >= 4:
                check = True
        if not check:
            total = 0
    elif ndx == 8: # Full house
        counts = set([roll.count(die) for die in roll])
        if 2 in counts and 3 in counts:
            total = 25
    elif ndx == 9: # Small straight
        for val in sorted(list(set(roll))):
            if last + 1 == val:
                count += 1
            last = val
        if count >= 4:
            total = 30
    elif ndx == 10: # Large straight
        for val in sorted(list(set(roll))):
            if last + 1 == val:
                count += 1
            last = val
        if count >= 5:
            total = 40
    elif ndx == 11: # Chance
        for val in roll:
            total += val
    else:
        if len(set(roll)) == 1:
            count = 50
    score_card[ndx][1] = total


def calc_score(score_card):
    new_total = 0
    for item in score_card:
        if type(item[1]) != str:
            new_total += item[1]
    return new_total

def still_moves(score_card):
    for item in score_card:
        if type(item[1]) == str:
            return True
    return False

while still_moves(score_card):
    choices = reset_choices()
    roll_1 = roller(5)

    for turn in range(3):
        roll_2 = merge_dice(new_choices, new_rolls, roll_1)
        printer(roll_1, choices, turn, score)
        new_choices = hold_die(roll_1, choices, turn)
        roll_again = count_holds(new_choices)
        if roll_again == 0 or turn == 2:
            break
        new_rolls = roller(roll_again)

    slot = available(score_card)
    write_score(score_card, roll_2, slot)
    score = calc_score(score_card)

print("Your final score is", score)
