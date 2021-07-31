class Details:
    def __init__(self):
        self.__id=1
        self.__name=""
        self.__gender=""
    def setDetails(self):
        self.__id=int(input("Enter Id: "))
        self.__name=input("Enter Name: ")
        self.__gender=input("Enter gender: ")
    def showDetails(self):
        print("Id: ",self.__id)
        print("Name: ",self.__name)
        print("Gender: ",self.__gender)

class Employee(Details):
    def __init__(self):
        self.__company=""
        self.__desig=""
    def setEmployee(self):
        self.setDetails()
        self.__company=input("Enter Compmany Name: ")
        self.__desig=input("Enter Designation: ")
    def showEmployee(self):
        self.showDetails()
        print("Company: ",self.__company)
        print("Designation: ",self.__desig)

class Doctor(Details):
    def __init__(self):
        self.__hospital=""
        self.__dept=""
    def setDoctor(self):
        self.setDetails()
        self.__hospital=input("Enter Hospital Name: ")
        self.__dept=input("Enter Department: ")
    def showDoctor(self):
        self.showDetails()
        print("Hospital: ",self.__hospital)
        print("Department",self.__dept)

def main():
    print("Employee Object: ")
    e = Employee()
    e.setEmployee()
    e.showEmployee()
    print("\nDoctor Object: ")
    d=Doctor()
    d.setDoctor()
    d.showDoctor()

if __name__=="__main__":
    main()