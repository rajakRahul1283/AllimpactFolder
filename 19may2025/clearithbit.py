n=11
i=1
if ((n&(1<<i))!=0):
     result=(n & ~(1<<i))
     print("after clear the ith bit:",result)
else:
     ("not clear")