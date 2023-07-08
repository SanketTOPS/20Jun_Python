fnm=input("Enter Firstname:")
lnm=input("Enter Lastname:")

if fnm.isalpha() and lnm.isalpha():
    email=input("Enter an Email Address:")
    if email.islower():
        #mobile=input("Enter a mobile Number:")
        pass
    else:
        print("Error!Plz input proper email")
    mobile=input("Enter your 10 digit mobile number:")
    if len(mobile)==10:
        print("Firstname:",fnm)
        print("Lastname:",lnm)
        print("Email:",email)
        print("Mobile:",mobile)
        print("------Data has been saved!------")
    else:
        print("Error!Plz enter valid mobile number")
else:
    print("Error!Something went wrong...Try again!")
    