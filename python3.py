#                                                             sreedhar
#                                                             1/01/2024

# syntax error
# try:
#     if()
#         print(input("enter the number"))
# except(SyntaxError):
#     print("Syntaxerror")


# type error
try:
    a = 2
    print(a+b)
except(NameError):
    print("NameError")

# value error
try:
    num = int(input("enter the number:"))
    num1 = int(input("enter the number1"))
    sum = num+num1
except(ValueError):
    print("ValueError")

try:
    a=3
    b="4"
    print(a+b)
except(TypeError):
    print("TypeError")
finally:
    print("finally  Error")

# try:
#     a=3
#     b=4
#     print(a+b)
# except(TypeError):
#     print("TypeError")
# else:
#     print("Error Removed")
#
# try:
#     a=3
#     b=4
#     print(a+b)
# except(TypeError):
#     print("TypeError")
# else:
#     print("Error Removed")
# finally:
#     print("god is great")


