#CS202 ASSIGNMENT 1
#DURGESH AGRAWAL AND SHIVAM KUMAR

#THIS FILE GENERATES BASIC CONSTRAINTS FOR THE SUDOKU (IN DIMACS FORMAT), I.E. ONE NUMBER IN EACH CELL,
#NO SAME NUMBERS IN A ROW/COLUMN/MAJOR DIAGONAL/SMALL 3*3 BOX.

a = [[0 for i in range(81)] for j in range(81)] #INITIALIZE CONNECTION ARRAY
count = 0

for i in range(81):
	for j in range(i-i%9, i-i%9+9):
		a[i][j]=1	#ROW-WISE CONNECTION
	for j in range(9):
		a[i][i%9+j*9]=1	#COLUMN-WISE CONNECTION
	row = (i/9)%3
	col = (i%9)%3
	for j in range(i/9 - row, i/9-row+3):
		for k in range(i%9 - col, i%9-col+3):
			a[i][j*9+k]=1	#SMALL SQUARE-WISE CONNECTION

for i in range(9):
	for j in range(9):
		a[i*9+i][j*9+j]=1
		a[i*9+8-i][j*9+8-j]=1	#DIAGONAL-WISE CONNECTION

open("basic_constraints.txt",'w').close()	#CLEAR PREVIOUS CONTENTS OF FILE
f=open("basic_constraints.txt", "a+")

for i in range(81):
	for j in range(9):
		f.write("%d"%(i*9+j+1))
		f.write(" ")
	f.write("0\n")
	count+=1	#EVERY CELL HAS AT LEAST ONE NUMBER
print(count)
for i in range(81):
	for j in range(9):
		for k in range(j+1,9):
			f.write("-%d -%d 0\n"%(i*9+j+1,1+i*9+k))
			count+=1	#NO CELL HAS MORE THAN ONE NUMBER
print(count)
for i in range(81):
	for j in range(0,i):
		if(a[i][j]==1):
			for k in range(9):
				f.write("-%d -%d 0\n"%(1+i*9+k,1+j*9+k))
				count+=1	#TWO CONNECTED ELEMENTS CANNOT HAVE SAME NUMBER
f.close()
print(count)
