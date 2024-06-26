
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020
}

# thisdict.update({"brand":"Ferrari"}) #update the values of the dictionary items

# thisdict.update({"color":"red&black"}) #if an value doesn't exist in the dictionary then it adds that value in the dictionary
# print(thisdict)
#print(thisdict.clear()) #remove all the elements from the dictionary

#a = thisdict.copy(); #returns a copy of dictionary
#print(a)

# print(thisdict.get("year"))
# print(thisdict["year"])

# both the methods works in the same way but when the key is not available then the get() returns the none and other one returns the error

# print(thisdict.get("year1"))
# print(thisdict["year1"])

#print(thisdict.items()) #returns a list containing a tuple for each key value pair

# print(thisdict.keys()) #returns all the dictionary keys

# print(thisdict.values()) #returns all the value of dictionary


# thisdict.pop("model"); #delete the specific element from the dictionary


thisdict.popitem(); #returns the last inserted key-value pair
print(thisdict)

