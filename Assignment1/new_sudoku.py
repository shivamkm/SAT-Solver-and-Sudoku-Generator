#CS202 ASSIGNMENT 1
#DURGESH AGRAWAL AND SHIVAM KUMAR

#THIS FILE GENERATES A NEW VALID SUDOKU EVERYTIME, SO THAT A PROBLEM CAN BE GENERATED OUT OF IT, FROM sud_gen.py

import os
import random

MINIMUM_CONS = 10773

basic_cons = open("basic_constraints.txt",'r')
basic_cons = basic_cons.read()	#BASIC CONSTRAINTS FOR EVERY SUDOKU

total_constraints = MINIMUM_CONS+9*9	#81 ADDITIONAL CONSTRAINTS ADDED TO GENERATE NEW SUDOKU

open("random_constraints.txt",'w').close()	#CLEAR PREVIOUS CONTENTS OF THE FILE
random_cons = open("random_constraints.txt",'a')

random_cons.write("p cnf 729 %d\n"%(total_constraints))
random_cons.write(basic_cons)

isconstrained = [0 for i in range(81)]

for iter in range(1,10):
	apply = random.randint(0,80)	#ITER ASSIGNED TO THIS POSITION
	while isconstrained[apply]==1:
		apply = random.randint(0,80)
	isconstrained[apply]=1

	for m in range(9):
		if iter==(m+1):
			random_cons.write("%d 0\n"%(9*apply+m+1))
		else:
			random_cons.write("-%d 0\n"%(9*apply+m+1))	#WRITE CONSTRAINTS CREATED DUE TO VALUE AT RANDOMLY GENERATED PLACE

random_cons.close()

os.system("./minisat random_constraints.txt sudoku.txt")

solution = open("sudoku.txt",'r').read().splitlines()
solution = solution[1].split(" ")
solution.pop()	#PARSE INTO ARRAY

sud2 = [[0 for i in range(9)] for j in range(9)]

for ll in range(729):
	if solution[ll][0]!='-':
		sud2[(ll/9)/9][(ll/9)%9]=ll%9+1

print " ________________________\n"
for i in range(9):
	for j in range(9):
		if(j%9==0):
			print "|",
		print sud2[i][j],
		if (j%3==2):
			print "|",
	print
	if (i%3==2):
		print " ________________________\n"	#PRINT SUDOKU IN A READABLE FORMAT
