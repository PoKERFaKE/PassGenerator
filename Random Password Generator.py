import random
try:
    password = int(input("Please Enter length of The password: "))

    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    p = "".join(random.sample(s,password ))
except:
    print("Please Enter a digit!!!")

else:
    print(p)
     


