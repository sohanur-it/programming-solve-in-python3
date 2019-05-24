#!/usr/bin/python3

T=int(input("Enter an input number :"))
for i in range(1,T+1):
	#print(i)
	N=int(input("value:"))
	if(N<10):
		lsb=N
		msb=0
	else:
		lsb=N%10
		div=int(N/10)
		while(div>10):
			div=int(N/10)
			N=div
			msb=div
	sum=0
	sum=lsb+msb
	print(sum)