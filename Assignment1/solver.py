#CS202 ASSIGNMENT 1
#DURGESH AGRAWAL AND SHIVAM KUMAR

#THIS FILE SOLVES A SUDOKU PROBLEM WITH THE INPUT FORMAT AS GIVEN IN THE ASSIGNMENT

#PROBLEM INPUT: A problem.txt FILE WITH '.' IN PLACES OF EMPTY CELLS AND NUMBERS 1-9 IN PLACES OF FILLED CELLS.
#ONE SPACE BETWEEN TWO CONSECUTIVE ENTRIES AND ROWS SEPARATED BY NEWLINE.

import os

MINIMUM_CONS=10773

f=open("problem.txt",'r')
problem = f.read().splitlines()

a = [[0 for i in range(9)] for j in range(9)]	#SUDOKU CONTENTS

ctr=0
add_cons=0	#CONSTRAINTS IN ADDITION TO BASIC CONSTRAINTS
for p in problem:
	row = p.split(" ")
	for q in range(9):
		if row[q] != '.':	#ACCOMODATE THE SPACES
			a[ctr][q] = int(row[q])
			add_cons+=9	#9 CONSTRAINTS FOR EACH VALUE SUPPLIED
	ctr+=1

total_cons = MINIMUM_CONS+add_cons

open("total_constraints.txt",'w').close()	#CLEAR PREVIOUS CONTENTS OF FILE
g=open("total_constraints.txt", "a+")

g.write("p cnf 729 %d\n"%(total_cons))

basic_constraints=open("basic_constraints.txt",'r').read()

g.write(basic_constraints)

for i in range(9):
	for j in range(9):
		if a[i][j]!=0:
			for k in range(9):
				if a[i][j]!=(k+1):
					g.write("-%d 0\n"%((i*9+j)*9+k+1))
				else:
					g.write("%d 0\n"%((i*9+j)*9+k+1))	#9 CONSTRAITS FOR EACH VALUE SUPPLIED, 8 NEGATIVE AND 1 POSITIVE

f.close()
g.close()

os.system("./minisat total_constraints.txt solution_sudoku.txt")	#CALL MINISAT

solution = open("solution_sudoku.txt",'r').read().splitlines()
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

