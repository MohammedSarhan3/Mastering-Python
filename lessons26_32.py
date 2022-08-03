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

#Task [4]

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

# Needed Output
print(set_two.issuperset(set_one))
#True

#Task [5]

# Create Dictionary Here
a={
    "HTML":"90%",
    "CSS": "90%",
    "Python": "30%"
}
# Needed Output


a["AI"] = "20%"
print(a.keys(),"Progress Is", a.values())
"HTML Progress Is 90%"
"CSS Progress Is 80%"
"Python Progress Is 30%"
"AI Progress Is 20%"