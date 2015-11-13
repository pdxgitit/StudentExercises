def test_var_args(f_arg, *argv):
    print ("first normal arg:", f_arg)
    for arg in argv:
        print ("another arg through *argv :", arg)

test_var_args('yasoob','python','eggs','test')




# Write a function that averages a variable number of arguments
# Don't forget your doc string






# Given an initial list (the first argument in your function), followed by one or more arguments.
# Remove all elements from the initial array that are of the same value as these arguments.

# i.e.:

# your_function([1, 2, 3, 1, 2, 3], 2 , 3) == [1, 1]
