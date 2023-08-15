class student:
    #Private
    __stid=12
    __stnm='Sanket'

    def __getdata(self):
        print(self.__stid)
        print(self.__stnm)
        print("This is getdata!")
    
    def printdata(self):
        self.__getdata()

st=student()
#st.getdata()

st.printdata()