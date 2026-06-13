# # # # print("Hii")


# # # #LIST  

# # # # ice_cream = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Cookies and Cream"]
# # # # print(ice_cream[-1])  

# # # # ice_cream.append("bulebeey")
# # # # ice_cream.insert(2, "Pistachio")
# # # # ice_cream.remove("Strawberry")
# # # # ice_cream.pop()
# # # # print(ice_cream)


# # # # for item in ice_cream:
# # # #     print(item)

# # # #TUPLE
# # #Immutable

# # # buildings = ("building1", "building2", "building3")

# # # buildings.append("building4")  # This will raise an AttributeError since tuples are immutable
# # # print(buildings[0])



# # #SET

# # #no duplicates

# # numbers = {1, 2, 3, 4, 5}
# # # numbers.add(6)
# # numbers.remove(3)
# # print(numbers)



# #DICTIONARY


# school = {
#     "name": "ABC School",
#     "add": "BBSR",
#     "build": 6,
#     "city": "BBSR"
# }

# school_address = school["add"]
# school["students"] = 1000
# # school.pop("city")

# # print(school.get("add"))
# # print(school.get("students"))

# for key,val in school.items():
#     print(key,val)



# String methods..........
 
name = "John"

# print(name.upper())
# print(name.lower())

# for char in name:
#     print(char)

name = name.replace("John", "Don")
print(name)