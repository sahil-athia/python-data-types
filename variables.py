# variable names cant not start with a number, contain spaces or particular characters
# python uses dynamic typing, the data type of a py var can be changed

random_thing = 10
print (random_thing)

random_thing = ["this", "is", "a", "list"]
print(random_thing)

# arithmatic with vars

a = 5
b = 10
print "before reassignment of var a:", a + b

a = a + a
print "after reassignment of var a:", a + b

# the type() function allows us to find out the data type of a given argument
print type(a), type(10.0)

# assigning vars with logic
my_income = 1000
tax_rate = 0.1
my_tax = my_income * tax_rate
print my_tax
