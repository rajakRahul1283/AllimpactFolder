def merge(num1,num2):
     i=0
     j=0
     result=[]
     while i < len(num1) and j < len(num2):
          if num1[i]< num2[j]:
               result.append(num1[i])
               i+=1
          else:
               result.append(num2[j])
               j+=1
     while i < len(num1):
          result.append(num1[i])
          i+=1
     
     while j < len(num2):
          result.append(num2[j])
          j+=1
          
          
     return result
          
          
print(merge([1,3,5,7], [2,5]))