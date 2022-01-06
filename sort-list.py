my_list = list('abcdef')

#sort method sort the list without returning list copy
my_list.sort(reverse=True)
print(f"my_list is : {my_list}")

#python sorted function returns sorted copy of the list
sorted_list = sorted(my_list)
sorted_list.insert(0,'z')
print(f"sorted_list is : {sorted_list}")
