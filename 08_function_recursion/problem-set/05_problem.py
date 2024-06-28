

def sum(a):
   if(a==1):
      return 1
   else:
      return sum(a-1)+a


a = sum(10);

print(a)