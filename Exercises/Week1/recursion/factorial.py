# Recursion is the process of breaking down a complex problem into a
# slightly smaller and similar problems until a base case is reached

# Example:

def fac(N):
    '''Calculate N factorial (N!) using recursion'''
    if N == 0:
        return 1
    else:
        return N * fac(N - 1)

print(fac(5))

# Write the function fib(N) which returns the Nth number in the fibonacci
# series.  Remember that when n is 1 fib(n) == 1 and when n is 0 fib(n) == 0.
# This should be used in your base case


# Write the function pow(base, power) which returns base^power
# pow (3, 1) == 3

# Questions:
#
# What should pow return for base=-5 and p=2?
# What should pow return for base=2 and p=-3?
# What would be a good base case for pow?
#     a) if p==0: return 0
#     b) if p==0: return 1
#     c) if p==0: return b
#     d) if p==1: return 0
#     e) if p==1: return 1
#     f) if p==1: return b
