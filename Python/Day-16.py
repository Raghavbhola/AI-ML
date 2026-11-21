#Multiple except block
# value = "0"
# try:
#     result = 100 / int(value)
#     print(result)
# # except ValueError:
# #     print("Value must be numeric")
# except Exception as e:
#     #print("Value must not be zero")
#     print(e)

# value = 2+3j
# result = 100 / int(value)
# print(result)
# try:
#     result = 100 / int(value)
#     print(result)
# # except ValueError:
# #     print("Value must be numeric")
# except Exception:
#     #pass
#     #print("Value must not be zero")
#     print(Exception)

#print("run successfully")

#Else-Finally block
# try:
#     num = int("abc")
# except ValueError:
#     print("Invalid number")
# else:
#     print("Valid number", num)
# finally:
#     print("validation done")

#Raise exception
# age = int(input("Enter age:-"))
# try:
#     if age<18:
#         raise ValueError("Age must be greater than 18")
#     print("Registration allowed")
# except ValueError as error:
#     print(error)

#Custom exception - Inherit a predefined class name as Exception
#import Exception
# class InsufficientBalanceError(Exception):
#     pass

# balance = 1000
# withdraw_amt = 1500
# try:
#     if withdraw_amt > balance:
#         raise InsufficientBalanceError("The withdrawing amount is higher than avl balance")
#     print("Amount withdrawn successfully")
# except Exception as error:
#     print(error)
