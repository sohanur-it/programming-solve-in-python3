#!/usr/bin/python3
T=input("enter the test values:")
T=int(T)
#print(T)
for i in range(1,T+1):
	print("case",i,":")
	N=input("enter a test value:")
	N=int(N)
	for j in range(1,N+1):
		if(N%j==0):
			print(j,end="  ")
	print("\n")
