n =0
while n <3:

    user = input("Username:")

    if user != "c4e":
        print("You are not superuser")
    else:
        password = input("Password:")
        if password == "abc":
            print("wellcome")
        else:
            print("Password is incorrect")
    n +=1
else:
    print("You filed to log in 3 times, go away")
