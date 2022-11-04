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

# ---------------------------------------------------------------------------------------------------------

# for x in range(5 + 1):
#     for y in range(3 + 1):
#         print(f"({x} , {y})")