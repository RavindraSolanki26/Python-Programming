s = {12,65,35,7.8,4551,232,"Ravindra",False};
d = {12,7.8,65,35,False}

# s.add(4554); #add an element to the set

# s.clear() #removes all the element form the set


# print(s.difference(d))

# print(s.intersection(d)); #returns value that is present in the  both sets 

# print(s.union(d)) #discard the values that is present in both sets 

# s.update(d); #(|=) we can use |= operator insted update also

# s |= d;
# print(s)

# print(s.pop()) #removes an element from the set

# s.remove(False); #remove an specific element


# z= s.issubset(d) #Return True if all items in set x are present in set d:
# z= d.issubset(s) # We can use the <= operator instead

# z = (d<=s)
# print(z)

z = s.issuperset(d) #Return True if all items set d are present in set s

# shortcut is >=

print(z)

