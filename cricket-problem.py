#!/usr/bin/python3
T=int(input("Enter the inputs:"))
for i in range(1,T+1):
	RR,CR,RB=input("<required run> <current run> <remaining balls> :").split(" ")
	RR,CR=[int(RR),int(CR)]
	RB=int(RB)
	balls_played=300-RB
	current_run_rate=(CR/balls_played)*6
	current_run_rate=round(current_run_rate,2)
	print("current run rate:",current_run_rate)
	required_run_rate=(((RR+1)-CR)/RB)*6
	required_run_rate=round(required_run_rate,2)
	print("required run rate :",required_run_rate)




