#you have a given a n*m row and column to find the supporter tree like apple
#if tree is not supporte print it is a mango tree
num=int(input("enter your no:"))
row,col=(3,4)
if num<=col:
     print("mango")
elif num%col==0:
     print("mango")
elif num%col==1:
     print("mango")
else:
     print("apple")