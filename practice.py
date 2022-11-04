# patient_name = "John Smith"
# age = 20 
# new_patient = True
# print(patient_name, age, new_patient)

# ---------------------------------------------------------------------------------------------------------

# name = input("What is your name? ")
# fav_color = input("What is your favorite color? ")
# print(f"{name} likes {fav_color}")

# ---------------------------------------------------------------------------------------------------------

# users_weight = input("What is your weight in Lbs? ")
# metric_weight = int(users_weight) * 0.45
# print(metric_weight) 

# ---------------------------------------------------------------------------------------------------------

# first = "pat"
# last = "murphy"
# msg = f"{first} {last} is a code"

# print(msg)


#  IF ELSE 
# ---------------------------------------------------------------------------------------------------------

# house_price = 1000000
# buyer_credit = False

# if buyer_credit:
#         credit = house_price *.1
#         print("You need a deposit of %10")
# else:
#         credit = house_price * .2
#         print("You need a deposit of %20")

# print(f"The total deposit payement is: €{credit}")

# ---------------------------------------------------------------------------------------------------------

# name = "paddy"

# if len(name) < 3:
#     print("Name must be at least 3 characters")
# elif len(name) > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("name looks good")

# ---------------------------------------------------------------------------------------------------------

# question = input("Weight: ")

# kilo_or_pounds = input("(L)bs or (K)g: ")

# if kilo_or_pounds == "k" or "K":
#     pounds = int(question) * 2.2
#     print(f"You are {pounds} pounds")
# elif kilo_or_pounds == "l" or "L": 
#     kilo = int(question) / 2.2
#     print(f"You are {kilo} kilos")

# ---------------------------------------------------------------------------------------------------------

# age = 22
# if age >= 18:
#     message = "Eligable"
# else: 
#     message = "Not Eligable"

            # OR
            
# age = 22
# message = "Eligable" if age >= 18 else "Not eligable"
# print(message)

# ---------------------------------------------------------------------------------------------------------

# high_income = True
# good_credit = False
# student = False

# if (high_income or good_credit) and not student:
#       print("Eligable")
# else:
#     print("Not eligable")

# ---------------------------------------------------------------------------------------------------------
# age = 22 
# if age >= 18 and age < 65:
#     print("Eligable")
    
            #OR
            
# if 18 <= age < 65:
#     print("Eligable")


# FOR LOOPS
# ---------------------------------------------------------------------------------------------------------

# for number in range(1, 20, 2):
#     print("apples", number)

# succesful = False

# for number in range(3):
#     print("Attempt")
#     if succesful:
#         print("succesful")
#         break
# else: 
#     print("Attempted 3 times and failed")


# FOR LOOPS
# ---------------------------------------------------------------------------------------------------------

# for x in range(5 + 1):
#     for y in range(3 + 1):
#         print(f"({x} , {y})")


# WHILE LOOPS
# ---------------------------------------------------------------------------------------------------------

# number = .01
# while number < 10000000:
#     print(number)
#     number *= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# INFINITE LOOP
# command = ""
# while True:
#     command = input("> ")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# count = 0
# for numbers in range(1, 10):
#     if numbers * 2 < 10:
#         even_number = print(numbers * 2)
#         count += 1
        
# print(f"we have {count} numbers")


# FUNCTIONS
# -----------------------------------------------------------------------------------------------------------  

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")
    
# greet("Paddy", "Murphy")

# Arguements - The actual value for the given parameter.
# Patameters - Input that is defined for the function.

# There are two types of functions.
# 1 - Preforms a task
# 2 - Calculate and returns a value

# Type 1.
# def greet(name):
#     print(f"Hi, {name}")

# Alter function type 1 to preform like type 2.
# def get_greeting(name):
#     return f"Hi, {name}"

# message = get_greeting("Paddy")
# print(message)
# file = open("content.txt", "w")       >>> Creates file named content.txt
# file.write(message)                   >>> writes value stored in message variable into the file.

# def increment(number, by):
#     return number + by
# Key word argument, makes code more readable. sounds like 2 by 1, which is 3.
# print(increment(2, by=1))

# def increment(number, by=1): >>> parameter that is used opionally 
#     return number + by 

# print(increment(15))

# def multiply(*numbers): >>> *numbers is used instead of multiple arguements to create 
#                         >>>  a tuple that is then used similarly as multiple parameters
#     print(numbers)

# multiply(2,3,4,5)


# def multiply(*numbers):
#     total = 1
#     for number in numbers: >>> iterates through the tuple.
#         print(number)      >>> Then prints each index.
#         total *= number
#     return total

# print(multiply(2,3,4,5))

#  