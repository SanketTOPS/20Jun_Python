import random

class student:

    def __init__(self) -> None:
        id=random.randint(1111,9999)
        print("Your ID is:",id)
    
    def getdata(self,name,city):
        print("Name:",name)
        print("City:",city)


st=student()
st.getdata('Sanket','Rajkot')