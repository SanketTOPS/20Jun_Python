import re

usernm=input("Enter an username:")
#Sanket2020

unm_pattern="[A-Z]+[a-z]+[0-9]"

x=re.findall(unm_pattern,usernm)

if x: #true
    print("Username is valid!")
else:
    print("Error! Invalid Username")
