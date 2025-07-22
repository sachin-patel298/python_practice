Pass = "Sachi78"
length = len(Pass)

if length < 6 :
    print("Password Is Weak")
elif length < 10 :
    print("Password Is Medium")
elif length > 10 :
    print("Password Is Strong")
