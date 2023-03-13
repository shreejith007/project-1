import random
otp =random.randint(10000,100000)

user =input("Enter your number ")
print("hello "+user)
print("Your One Time Password is"+str(otp)
      +"Plz dont share it with any one else .Thank You...")
password=input("Enter the Otp to login:")
if password == str(otp):
    print("Login Succesflly ")
else:
    print("Login Failed")   