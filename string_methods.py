# strings are immutable, so this is how to change them, reassign Sam to Pam

name = "sam"
final_letters = name[1:] #am
new_name = "P" + final_letters
print(new_name)

# string contatenation
# we can also sdo multiple string contatenatio
letter = "z"
print letter * 10

# using the string methods

x = "Hello World"

print x.upper() 
print x.lower()
print x.split() # create a list, we can give a place to split upon with a parameter
print x.split("o") # this will split at all of the "o"'s


# print methods and formatting
# the format method is similar to template literals in JS

print "this is a string {} {} {}".format("with", "some", "insertions")

# we can supply words in a particular order

print "printing in order {1} {0} {2}".format("2", "1", "3")

# we can give varibale assignments to the inserted words

print "fruits: {a} {b} {c}".format(a = "apple", b = "banana", c = "cantelope")

# formatting floats syntax: {value:width.percision f}

random_float = 0.123412341234
print "result is: {r:1.3f}".format(r = random_float)
# the percision is what will be changed most of the time, the width adds whie space to give the string number

# f-strings are formmated string literals
name = "joe"
print (f'Hello my name is {name}')