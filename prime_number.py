#!/usr/bin/python3

T=int(input("How many iteration you want:"))
for i in range(1,T+1):
	min,max=input("value of minimum and maximum:").split(" ")
	min,max=[int(min),int(max)] 
	count=0
	for j in range(min,max+1):
		for k in range(2,j):
			if(j%k==0):
				break
			else:
				print(j,"\t")
				count=count+1
				break
	print("count=",count)

