import random

class student:
    def __init__(self,name) -> None:
        id=random.randint(1111,9999)
        print("ID:",id)
        print("Name:",name)

st=student('Sanket')
