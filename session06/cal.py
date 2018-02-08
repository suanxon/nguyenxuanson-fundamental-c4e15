def eval (x, y, op): # tham so dau vao cua ham


    result = 0
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == '*':
        result = x * y
    elif op == "/":
        result = x / y
    return result

x = int(input("x = "))
y = int(input("y = "))
op = input("Operation?")

result = eval(x, y, op)
print("{0} {1} {2} = {3}".format(x, op, y, result))

# x = int(input('x = '))
# operation = input("operation(+,-,*,/)")
# y = int(input('y = '))
#
# if operation == "+":
#     a = x + y
# elif operation == "-":
#     a = x - y
# elif operation == "*":
#     a = x * y
# elif operation == "/":
#     a = x / y
# else:
#     print("Error")
#
# print("* " * 10)
# print(x, operation, y, "=", a )
# print ("* " * 10)
