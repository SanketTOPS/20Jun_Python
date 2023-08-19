import re

email=input("Enter an email:")
#sanket@gmail.com

email_pattern="^[a-z0-9]+[@]+[a-z]+[\.]+[a-z]"

x=re.findall(email_pattern,email)

if x: #true
    print("Valid Email!")
else:
    print("Error! Invalid Email address")