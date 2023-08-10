class student:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)


st=student()
#st.getdata(12,'Sanket')
stid=input("Enter an ID:")
stnm=input("Enter a Name:")
st.getdata(stid,stnm)
