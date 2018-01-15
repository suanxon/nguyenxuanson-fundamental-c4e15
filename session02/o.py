from getpass import getpass
print("Hi there, this is a superuser gateway")
x = "C4E"
y = "codethechange"
user = input("Username:")
password = input("Password:")

if user == x:
    if password == y:
        print("Welcome, c4e")
    else:
        print("Password is incorrect")
else:
    print("You are not superuser")
