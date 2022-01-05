#Copy a list to other list
my_list = ['a','b','c']
other_list = my_list.copy()
other_list.append('d')
my_list.append(123456)

print(f"my_list contents are : {my_list}")
print(f"other_list contents are : {other_list}")

print("")
print("###################################")
print("")

#List Assignment
a_list = ['a','b','c']
b_list = a_list
b_list.append('d')
a_list.append(123456)

print(f"a_list contents are : {a_list}")
print(f"b_list contents are : {b_list}")
