my_list = [1, 2, 3, 4, 5]
my_other_list = ["still", 1, "a", "list", 3]

print ("my other list is {} elements long".format(len(my_other_list)))
print my_other_list[2]
print my_other_list[:2]

# concatenating lists

print my_list + my_other_list

my_list[2] = "changed"
my_list.append(6)
print my_list

# pop can remove specific indexes

new_list = ["e", "t", "a", "p"]
num_list = [2, 1, 5, 3]

new_list.sort() 
# changes the list in place so its result cant be 
# reassigned to something needs to be called before reassignment
print new_list


new_list.reverse()
print  new_list