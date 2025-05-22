digits=[2,3,1,0]
result=[]
for i in range(len(digits)):
     for j in range (len(digits)):
          for k in range (len(digits)):
               if i!=j and j!=k and k!=i:
                    a,b,c=digits[i],digits[j],digits[k]
                    if a!=0 and c%2==0:
                         num=a*100+b*10+c
 
                         result.append(num)
                         
result.sort()                         
print(result)

                    
                         