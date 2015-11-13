from turtle import *    # loads the turtle library...
import time

# width(5)        # make the turtle pen 5 pixels wide
# shape('turtle') # use a turtle shape!
# forward(100)    # turtle goes forward 100 steps
# right(90)       # turtle turns right 90 degrees
# up()            # turtle lifts its pen up off of the paper
# forward(100)    # turtle goes forward 100 steps
# down()          # turtle puts its pen down on the paper
# color("red")    # turtle uses red pen
# circle(100)     # turtle draws circle of radius 100
# color("blue")   # turtle changes to blue pen
# forward(50)     # turtle moves forward 50 steps



# def poly(n, N):
#     """ draws n sides of an N-sided regular polygon """
#     if n == 0:
#         return
#     else:
#         forward( 50 )   # 50 is hard-coded at the moment...
#         left( 360.0/N )
#         poly( n-1, N )
#
# poly(7, 7)

# branching-recursion: It's in branching that recursion is at
# its most "magical"—but it's also true that in composing these
# functions, it can be the most mind-bending. What's remarkable is that
# the "magic" is, in the end, completely understandable.

# Run the following function at least four times.
# uncomment the line that says input().
# You need to press ENTER to exit turtle

# 1 - as it is currently constructed
# 2 - uncomment the first branch(size/2)
# 3 - uncomment the second branch(size/2)
# 4 - change the second call to branch(size/3)

# Feel free to add color changes or line-width changes (or both)

# We are creating a smaller version of the overall structure at more
# than one location within that structure.

# The key to making "branching-recursion" work is making sure that your
# turtle ends at the same location that it begins. That is how you know
# that the statements after the recursive calls are moving the turtle
# as expected.

# def branch(size):
#     """ branching recursion function! """
#     if (size<9):
#         return
#     else:
#         forward(size)
#         left(90)
#         forward(size/2.0)
#         right(90)
#         # branch(size/2)
#         right(90)
#         forward(size)
#         left(90)
#         # branch(size/2)
#         left(90)
#         forward(size/2.0)
#         right(90)
#         backward(size)
#         return
#
# branch(100)
# # input()

# A lot of methods can be re-written using recursion. For example below
# the len() method has been rewritten as re_len() using only recursion.

# def re_len(s):
#     '''Input: string -> Ouput: length of string'''
# 	    if s == '':
# 	        return 0
# 	    else:
# 	        return 1 + re_len(s[1:])
#
# test = re_len('pdx')
# print ('test length is', test)


# One more example.
def drawFlake(length, depth):
    """ fractal snowflake function
        length: pixels in the largest-scale triangle side
        depth: the number of recursive levels in each side
    """
    if depth == 0:
        forward(length)
    else:
        drawFlake(length/3, depth-1)
        right(60)
        drawFlake(length/3, depth-1)
        left(120)
        drawFlake(length/3, depth-1)
        right(60)
        drawFlake(length/3, depth-1)


drawFlake(500, 4)
input()
