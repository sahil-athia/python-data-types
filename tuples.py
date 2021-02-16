# much like lists but they are immutable
# we use parenthesis instead of []

t = (1, 2, '3')
l = [1, 2, 3, 4]

print type(t), len(t), t[1]
print type(l), len(l)

random_letters = ("a", "a", "b", "e")
print random_letters.count("a")
print random_letters.index("a")

# index will return index of the first instance of an element