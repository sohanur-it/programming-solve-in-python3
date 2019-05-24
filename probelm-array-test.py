#!/usr/bin/python3
memo=[] 
n=int(input("Enter the value of n :"))
for i in range (n):
    x=int(input("enter no. \n")) 
    memo.insert(i,x)
    i+=1
print(memo) 
