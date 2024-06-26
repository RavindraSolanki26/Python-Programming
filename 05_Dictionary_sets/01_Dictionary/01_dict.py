
# dictionary is a collection of key:value pair
# in dictionary keys are unique and values can be duplicate
# dictionary is mutable which means we can change the dictionary items

# dict = {} #this is how we create the empty dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  #"year": 1964, #duplicate items are not allowed
  "year": 2020
}
# print(type(thisdict))
# print(thisdict)

print(thisdict["model"]) #accessing the dictionary items

thisdict["year"] = 2020; #changing the values of dictionary items
print(thisdict)
# print(dict)


# creating ditionary usign the dict() constructor

# new_dict = dict({1:100,2:200,3:300,4:400});
# print(new_dict)
# print(type(new_dict))