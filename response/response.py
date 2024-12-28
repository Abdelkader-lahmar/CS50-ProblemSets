from validators import email

user_input = input("What's your email address? ")
if email(user_input):
    print("Valid")
else:
    print("Invalid")
