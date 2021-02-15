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