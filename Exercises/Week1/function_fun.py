# The string inside triple quotes """ is called the docstring,
# short for "documentation string." I will ask you to include a
#  docstring in all of your functions (create good habits).
#
# A docstring should describe what the function outputs and
# what the function inputs. As you see below, it may include
# other important information, too.


def dbl(x):
    """  output: dbl returns twice its input
         input x: a number (int or float) or a string
         Spam is great, and dbl("spam") is better!
    """
    return 2*x

print (dbl("spam"))

# Write the function tpl(x), which takes in a numeric input and outputs three
# times that input.

# Write sq(x), which takes in a number named x as input. Then,
# sq should output the square of its input.  You will have to
# import the math library.  math.sqrt(9) == 3


# Write the funtion interp(low,hi,fraction). It takes in three
# numbers, low, hi, and fraction, and should return the
# floating-point value that is fraction of the way between low
# and hi.

# if fraction is zero, low will be returned. If fraction is one,
# hi will be returned, and values of fraction between 0 and 1
# will lead to results between low and hi.

# Examples: 
# interp(1.0, 9.0, 0.25) -a quarter (.25) of the way from 1.0 to 9.0
# == 3.0
#
# interp(1.0, 3.0, 0.25) -a quarter of the way from 1.0 to 3.0
# == 1.5
#
# interp(2, 12, 0.22)    -22% of the way from 2 to 12
# == 4.2
