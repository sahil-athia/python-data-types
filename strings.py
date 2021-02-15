# strings can be indexed and sliced, indexing starts at 0
# example: "hello", regular index: 0, 1, 2, 3, 4, reverse index: 0, -4, -3, -2, -1

greeting = "hello"
print "hello \nworld \n", "hello \t world" # n for newline t for tab
print greeting # will say hello
print greeting[1] # will say 'e'
print greeting[-1] # will say '0'
print len(greeting) # length function

# slicing lets us grab a subsection of characters, syntax: [start:stop:step]
# start is the index of where we start
# stop is where we go up to (but not include)
# step is the size of the jump

my_string = "abcdefghijk"
print my_string
print my_string[2:] # from 2 all the way to the end
print my_string[:3] # will give back abc [0:3]
print my_string[3:6] # will give back def

print "setting the step size"
print my_string[::] # from 0 to end with a step size of 1
print my_string[::2] # from 0 to end with a step size of 2
print my_string[::-1] # this can be used to reverse a string since the step size is -1