# Design your own Adventure Game
#
# The goal of the Adventure Game is to create a purely text-based game based on
# conditionals. More specifically, you are using if/else statements to create an
# exploratory and interactive story game. Adventure Games are extremely neat
# because they can be rather simple or very complex, and could be used to depict
# a variety of topics (You are welcome to look at the Python Textbook for a basic
# idea/starting point). Feel free to pull from literature, video games,
# television, or movies!
#
# The first step would be to design a map for your Adventure Game and decide
# which paths would lead to successfully completing your challenge and which
# paths would leads to dead ends, and how all of the areas are connected.


print('''You enter into Candyland.''')
print('''Where do you want to go?''')

action = input ('''Type: Peppermint Forest, Gingerbread Tree, or Gumdrop
    Mountains. Then press enter. ''')

if action == '''Peppermint Forest''':
    print('''You enter Peppermint Forest. You are surrounded by white and red.
        You are kept in the shade by giant candy canes.''')
    print('''Now,where do you want to go?''')

    action = input ('''Type: Gingerbread Tree, Gumdrop Mountains, Licorice
        Jungle. Then press enter.''')

if action == '''Gingerbread Tree''':
    print('''You are at Gingerbread Tree, the largest and oldest tree in the
        entire Candyland. You grab some gingerbread to go. The Gingerbreads
        have a parade currently, and the only route you can take is to
        Peppermint Forest ''')

    action = '''Peppermint Forest'''

if action == '''Gumdrop Mountains''':
    print('''You successfully reached Bubblegum peak. However, to continue, you
    must go through the Gumdrop Pass. Gumdrop is a shortcut to reaching Candy
    Castle. However, the pass is very unsafe and not advisable. If you would
    like, you can choose to go another route.''')

    action = input ('''Type: Gingerbread Tree, Gumdrop Pass, Licorice Jungle.
    Then press enter.''')

if action == '''Licorice Jungle''':
    print('''You have reached Licorice Jungle. However, you are stuck in Licorice
    Swamp and cannot move on. Lord Licorice finds you in his territory and
    sends you back to Peppermint Forest''')

    action = '''Peppermint Forest'''

if action == '''Gumdrop Pass''':
    print('''Despite almost falling the very narrow and slippery Pass, you made
    it through Gumdrop pass. Good job!''')
    print('''Now, where do you want to go?''')

    action = input ('''Type: Chocoville, Lollipop Woods. Then press enter.''')

if action == '''Chocoville''':
    print('''You enter Chocoville, a land filled with every type of chocolate
    imaginable. In fact, Grandma Cocoa feeds you chocolate all day that you
    become tired of chocolate and decide to leave. You encounter the fields of
    Cotton Candy City. ''')

    action = '''Cotton Candy City'''

if action == '''Cotton Candy City''':
    print('''You are fascinated by the thousands of acres of Cotton Candy plants.
    You decide to stay there and learn how to grow Cotton Candy. Afterwards,
    you head on to Lollipop Woods.''')

    action = '''Lollipop Woods'''

if action == '''Lollipop Woods''':
    print('''You finally reach Lollipop Woods, filled with millions of lollipops
    of various flavors, colors, and sizes. You then meet Lolly fairy, who
    builds you your own house made out of lollipops. You then follow the Yellow
    Lollipop road, only to find out that you have finally reached Candyland
    Castle. CONGRATULATIONS!''')
