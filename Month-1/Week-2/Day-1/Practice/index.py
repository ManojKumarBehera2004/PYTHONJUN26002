# # # # print("OOP concept")

# # # #Make an object class

# # # class Car:
# # #     cat = "SUV"
# # #     color = "Red"
# # #     wheel = 4

# # # car1 = Car()

# # # print(car1.cat)
# # # print(car1.color)


# # #Methods

# # class Student():
# #     name = "Rahul"
# #     age = 21
# #     def StudentDetails(self):
# #         print("Student name is", self.name , "age is", self.age)
# #     def viewinput(self, address, roll):
# #         print("This is the address", address, "This is the roll", roll)     
# #     s1 = Student()

# #     print(s1.age)

# #     s1.StudentDetails()
# #     s1.viewpoint("Bhubaneswar",40)
    

# #Constructor



# class Citizen:
    
#     def __init__(self, aadhar, phone, name):
#         self.aadhar = aadhar
#         self.phone = phone
#         self.name = name

#     def printCitizen(self):
#         print("Aadhar -" , self.aadhar)
#         print("Phone -" , self.phone)
#         print("Name -" , self.name)
    
# c1 = Citizen("3647748666", "12345677889", "Prakash")
# c2 = Citizen("1234509876", "1122334455", "Manoj")
# c3 = Citizen("6655443322", "3388990077", "Rahul")

# c2.printCitizen()


class Building:
    country = "India"

    def __init__(self):
        self.location = input("Enter location: ")
        self.pin = input("Enter pincode: ")
        self.floor = input("Enter floor count: ")
        self.roomInFloor = input("Enter room in each floor: ")

        print("country -", self.country)
        print("Location -", self.location)
        print("Pin -", self.pin)
        print("Floor -", self.floor)
        print("Room -", self.roomInFloor)
b1 = Building()

