import random
import os

MINIMUM_CONS=10773

def print_sud(sudoku):
	open("generated_problem.txt",'w').close()
	f = open("generated_problem.txt",'a')
	sud2 = [['.' for i in range(9)] for j in range(9)]

	for ll in range(81):
		if sudoku[ll]!=0:
			sud2[ll/9][ll%9]=sudoku[ll]

	print " ________________________\n"
	f.write(" ________________________\n\n")
	for i in range(9):
		for j in range(9):
			if(j%9==0):
				print "|",
				f.write("| ")
			print sud2[i][j],
			f.write("%s "%(sud2[i][j]))
			if (j%3==2):
				print "|",
				f.write("| ")
		print
		f.write("\n")
		if (i%3==2):
			print " ________________________\n"
			f.write(" ________________________\n\n")
	f.close()

#MAIN PROGRAM THAT GENERATES PROBLEM
def driver(i):

	global deleted

	open("total_constraints.txt",'w').close()	#CLEAR PREVIOUS CONSTRAINTS
	h = open("total_constraints.txt",'a+')

	memory = sud[i]	#STORE RECENTLY DELETED ENTRY
	sud[i]=0
	deleted+=1

	total_cons = MINIMUM_CONS + 9*(81-deleted)

	h.write("p cnf 729 %d\n"%(total_cons+1))
	h.write(basic_cons)

	for j in range(81):
		if sud[j]!=0:
			for m in range(9):
				if sud[j]==(m+1):
					h.write("%d 0\n"%(9*j+m+1))
				else:
					h.write("-%d 0\n"%(9*j+m+1))	#WRITE CONSTRAINTS CREATED DUE TO KNOWN VALUES OF SUDOKU

	for iter in range(i*9,i*9+9):
		if arr[iter][0]=='-':
			h.write("%d "%(iter+1))
		else:
			h.write("-%d "%(iter+1))
	h.write("0\n")	#CONSTRAINT THAT SUDOKU HAS TO BE DIFFERENT

	h.close()

	os.system("./minisat total_constraints.txt is_unique.txt")

	is_unique = open("is_unique.txt",'r').read()
	satisfiability_array.append(is_unique[0])

	if is_unique[0]=="S":	#MORE THAN ONE SOLUTION IS POSSIBLE, UNFAVOURABLE AND WE MUST RESTORE THE LAST DELETED ELEMENT
		deleted-=1
		sud[i]=memory

f = open("sudoku.txt",'r')	#COMPLETELY SOLVED SUDOKU IN MINISAT'S OUTPUT FORM
cont = f.read().splitlines()[1]
arr = cont.split(" ")
arr.pop()
f.close()

sud = []

for i in range(729):
	if arr[i][0]!="-":
		sud.append(i%9+1)	#SUDOKU AS AN ARRAY OF LENGTH 81

basic_cons = open("basic_constraints.txt",'r')
basic_cons = basic_cons.read()	#BASIC CONSTRAINTS FOR EVERY SUDOKU

satisfiability_array=[]

deleted=0	#NUMBER OF ENTRIES DELETED

for k in range(81):	#LARGE NUMBER OF ITERATIONS ENSURE THAT PROBLEM SUDOKU GENERATED IS MINIMAL WITH HIGH PROBABILITY
	i = random.randint(0,80)
	while(sud[i]==0):
		i = random.randint(0,80)	#ENTRY TO BE DELETED
	driver(i)

for k in range(81):	#DETERMINISTIC PASS OVER THE SUDOKU TO ENSURE THAT THE GENERATED SUDOKU IS MINIMAL
	if sud[k]!=0:
		driver(k)

print_sud(sud)	#PRINT GENERATED SUDOKU IN READABLE WAY

print satisfiability_array[:81]	#SATISFIABILITY DATA FOR THE ITERATIONS WHEN RANDOM NUMBERS WERE REMOVED
print satisfiability_array[81:]	#SATISFIABILITY DATA FOR THE ITERATIONS WHEN A DETERMINISTIC PASS WAS TAKEN

