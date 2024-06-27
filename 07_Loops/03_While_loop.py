#while (condition): # The block keeps executing until the condition is true
#Body of the loop

# i = 0;
# while(i<11):
#     print(i)
#     i+=1;


# Iteration on list

# li = [1,2,3,4,5,6];

# i = 0;
# while(i<len(li)):
#     print(li[i])
#     i+=1;


# Iteration on Tuple

# tu = (12,13,14,15,16,17,18,19,20)

# i = 0;
# while(i<len(tu)):
#     print(tu[i])
#     i+=1;


# in while loop we can't iterate on set directly for this first we have to convert set into another datatype and later we can iterate on that

se = {12,13,14,15,16};

#converting set into list

# li = list(se);

#converting set into tuple

# tu = tuple(se)

# i = 0;

# while(i<len(tu)):
#     print(tu[i])
#     i+=1;


# --------break, continue and pass ------

#break
# i = 0;
# while(i<10):
#     i+=1;
#     if(i==4):
#         break
#     print(i)


i = 100;

while(i>0):
    i-=1;
    if(i==3):
        continue
    print(i)