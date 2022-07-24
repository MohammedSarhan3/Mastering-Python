Add First Task
#1
#name= "'osama'"
age = '"18"'
coun= "egypt"

#print("Hello" +name + ", How You Doing \\" 
#'""" ' 'Your Age Is'+ age +'"'" +
#\And Your Country Is:" + coun)

#2
name = 'Elzero'
# Needed Output
# Second Letter Is "l"
print(name[1])
# Third Letter Is "z"
print(name[2])
# Last Letter Is "o"
print(name[5])

#3
# Needed Output
# "lze"
print(name[1],name[2],name[3])
# "Ezr"
print(name[0],name[2],name[4])
# "rzE"
print(name[4],name[2],name[0])


#4
name2 = "#@#@Elzero#@#@"

# Needed Output
# Elzero
print(name2.replace("#@", ""))

#5
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

# Needed Output
# 0009
print(num1.zfill(4),num2.zfill(4),num3.zfill(4),num4.zfill(4),num5.zfill(4))
# 0015
# 0130
# 0950
# 1500

#6

name_one = "Osama"
name_two = "Osama_Elzero"

# Needed Output
print(name_one.rjust(20, "@"))
# @@@@@@@@@@@@@@@Osama
print(name_two.rjust(20, "@"))
# @@@@@@@@Osama_Elzero

#7
name_one = "OSamA"
name_two = "osaMA"

# Needed Output
# osAMa
print(name_one.swapcase())
# OSAma
print(name_two.swapcase())

#8
msg = "I Love Python And Although Love Elzero Web School"

# Needed Output
print(msg.count("Love"))
# 2

#10
name = "Elzero"

# Needed Output
print(name.index("z"))
# 2

#11

msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although <3 Elzero Web School
print(msg.replace("<3", "Love",1))


