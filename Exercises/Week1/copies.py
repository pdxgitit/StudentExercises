# id returns the unique integer that represents the "identity" of
# an element.

# x = 3
# y = x
#
# print(x, y)
# print(id(x), id(y))
#
# x = 5
#
# print(x, y)
# print(id(x), id(y))
#
colors = ["red", "green"]
colors2 = colors

print (colors)
print (colors2)
#
print(id(colors), id(colors2))
#
colors2 = ["orange", "yellow"]

print (colors)
print (colors2)

print(id(colors), id(colors2))
#
colors = ["red", "green"]
colors2 = colors

colors2[1] = "blue"

print (colors)
print (colors2)

print(id(colors), id(colors2))
