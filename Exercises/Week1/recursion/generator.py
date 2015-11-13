# Generators are an advanced topic. They rely heavily on recursion.
# Most importantly - they don't return once which would force them to
# store a large data set in memory.  Instead or returning a value they
# yield and then continue processing

def getPermutations(string):
    if len(string) == 1:
        yield string
    else:
        for i in range(len(string)):
            for perm in getPermutations(string[:i] + string[i+1:]):
                yield string[i] + perm

all = getPermutations("abcdefgjdflk;ghgkld;fshgeoi[gehrg]")

for item in all:
    print(item)
