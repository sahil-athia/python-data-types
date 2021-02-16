my_file = open('test.txt')

print my_file.read()
# after reading a file we have to reset the cursor to re-read it
my_file.seek(0)
print my_file.read()

my_file.seek(0)
print my_file.readlines()
# readlines will create a list of out file

# since we opened out file it is best practice to close it
my_file.close()

# we can also use a with statement to use the file in a specific location (now we dont need to close)
with open("test.txt") as my_new_file:
  print my_new_file.read()

# we can also write to and overwrite files

# this is reading a file 
with open("test.txt", mode="r") as f:
  print f.read() 

# this is appending to a file 
with open("test.txt", mode="a") as f:
  f.write("\nthis is the fourth line")

with open("test.txt", mode="r") as f:
  print f.read()  

# this is writing to a file 
with open("new_file.txt", mode="w") as f:
  f.write("i created this file")

with open("new_file.txt", mode="r") as f:
  print f.read() 

  
# # this is reading and writing to a file 
# with open("test.txt", mode="r+") as my_new_file:

# # this is reading and writing to a file and will overwirite files or create new ones
# with open("test.txt", mode="w+") as my_new_file: