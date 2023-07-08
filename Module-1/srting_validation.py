"""unm="admin"
pas="admin"

username=input("Enter an username:")
password=input("Enter a Password:")

if username==unm and password==pas:
    print("Login Successfull!")
else:
    print("Error!Login fail..")"""

# ------------------------------------------- #

fnm=input("Enter Firstname:")
lnm=input("Enter Lastname:")


if fnm.isalpha() and lnm.isalpha():
    print("Done...Plz fill up email and mobile details now!")
    email=input("Enter an Enamil:")
    mobile=input("Enter a mobile number:")
    if email.islower() and mobile.isdigit():
        print("Firstname:",fnm)
        print("Lastname:",lnm)
        print("Email:",email)
        print("Mobile:",mobile)
        print("---------Your data has been submitted!---------")
    else:
        print("Error!Please enter proper details")