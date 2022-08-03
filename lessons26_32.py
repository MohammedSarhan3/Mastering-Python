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

#Task [2]
nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3, "A", "B", "C"}

print(nums | letters)

# {1, 2, 3, "A", "B", "C"}
print(letters.union(nums))
# {1, 2, 3, "A", "B", "C"}

print(nums.union(letters))

#Task [3]
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output
print(my_set)
# {1, 2, 3}

# set()
a=my_set.clear()
print(a)
# {"A", "B"}
my_set.add("A")
my_set.add("B")
print(my_set)