#!/usr/bin/python3

T=int(input("Enter an input number :"))
for i in range(1,T+1):
	#print(i)
	N=int(input("value:"))
	for j in range(1,N+1):
		for k in range(1,N+1):
			print("*",end=" ")
		print("\n")
