#Assignments For Lessons 26 To 32
#Task [1]

my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output

# 1, 2, 3, 4, 5
unique_list=set(my_list)
print(unique_list)
# <class 'list'>
print(type(list(unique_list)))
# 1, 2, 3, 4
g=unique_list.remove(5)
print(g)