#Assignments For Lessons 41 To 46
# Task [1]

# Inputs
'''
#num1 = int(input("Enter The Fisrt Number: ").strip())
#num2 = int(input("Enter The Secound Number: ").strip())
#operation = input("Enter Operation: ").strip()
#"+" Or "-" Or "*" Or "/" Or "%"
# Needed Output
if operation == "+":
    nums =num1 + num2
    print(f"[{num1}][{operation}][{num2}][={nums}]")
if operation == "-":
    nums =num1 - num2
    print(f"[{num1}][{operation}][{num2}][={nums}]")
if operation == "*":
    nums =num1 * num2
    print(f"[{num1}][{operation}][{num2}][={nums}]")
if operation == "/":
    nums =num1 / num2
    print(f"[{num1}][{operation}][{num2}][={nums}]")
if operation == "%":
    nums =num1 % num2
    print(f"[{num1}][{operation}][{num2}][={nums}]")

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800

'''


#Task [2]
age = 6

# Needed Output

print ("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")
#"App Is Suitable For You" # If Age Larger Than 16
#"App Is Not Suitable For You" # if Age Smaller Than 16


#Task [3]
'''
# Input Example 38
age = int(input("Enter Your Age: ").strip())
# Needed Output
if age > 10 and age <100 :
    monthe = age * 12
    week= age * 48
    print(f"Your Age In Months Is {monthe} Months")
    print(f"Your Age In Weeks Is {week} Weeks")
else:
    print("Your Age Out Of The Range.")
#"Your Age In Months Is 456 Months" # Months Example
#"Your Age In Weeks Is 1824 Weeks" # Weeks Example

'''

#Task [4]
# Input Example One "Egypt"
# Input Example Two "Ghana"

country = input("Input Your Country:  ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = price - 30
if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${discount}")
else:
    print("Your Country Not Eligible For Discount And The Price Is $100")
# Needed Output
"Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
"Your Country Not Eligible For Discount And The Price Is $100" # Ghana Example