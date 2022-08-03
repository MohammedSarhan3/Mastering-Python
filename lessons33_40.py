#Assignments For Lessons 33 To 37

print("Assignments For Lessons 33 To 37")
#Task [1]
# True Values

print(bool("Osama"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print("=" * 50)


#Task [1]
# True Values

print(bool("Osama"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print("=" * 50)

# False Values

print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool({}))
print(bool(None))

print("=" * 50)
# Task [2]
html = 80
css = 60
javascript = 70

# Needed Output
#True
print(html>50 and css>50 and javascript>50)


print("=" * 50)


# Task [3]
num_one = 10
num_two = 20
num = 20

# Needed Output

#True
print(num>num_one or num > num_two)
#False
print(num>num_one and num > num_two)


print("=" * 50)



# Task [4]
num_one = 10
num_two = 20

# Needed Output

30
result =  num_one+num_two
print(result)
27000
Exponent = result**3
print(Exponent)
1000
e= Exponent/26000
print(e)
200.0
#<class 'str'>
print("=" * 50)


#Assignments For Lessons 38 To 40

print("Assignments For Lessons 38 To 40")


# Task [1]
# Input
name = input("Ener your name").strip().capitalize()
"     osAmA   "

# Needed Output
print(f"Hello {name}, Happy To See You Here.")
"Hello Osama, Happy To See You Here."
print("=" * 50)

# Task [2]
# Inputs
age= int(input("enter your age: "))
16 # Input One
ag=age <16
24 # Input Two
f= age > 16
# Needed Output
print(f"Hello Your {ag} Is Under 16, Some Articles Is Not Suitable For You" )

print(f"Hello Your Age Is {f}, All Articles Is Suitable For You" )

"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" # If Age < 16
"Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You" # If Age Is 16+
print("=" * 50)


# Task [3]
# Inputs

"Osama" # First Name
FirstName = input("Enter your First Name: ").capitalize()
"Mohamed" # Second Name
SecondName = input("Enter your Second Name: ")
# Needed Output

"Hello {First_Name} {First_Letter_From_Second_Name}." # Example "Osama M."
print(f"Hello {FirstName} {SecondName:.1s}.") 


print("=" * 50)