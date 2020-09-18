Language: Python

How to build:
Paste the four .py files in the 'core' folder of minisat. Also, paste the problem.txt file in the same folder if you wish to solve sudoku using this.

STEP 1: Run `python gen_basic_cons.py` to generate the basic constraints for a sudoku as given in the assignment.
To solve sudoku -
STEP 2: Run `python solver.py` and the solution will appear on the terminal and will also be saved in solution_sudoku.txt. The DIMACS representation of the constraints will be stored in total_constraints.txt.
To generate problem -
STEP 2: Run `python new_sudoku.py` to create the solution to the problem to be generated. Each time, a new sudoku will be created. It will also be stored in sudoku.txt and the corresponding constraints will be stored in random_constraints.txt.
STEP 3: Run `python sud_gen.py` to generate a minimal problem with the solution from sudoku.txt. The problem will appear in the terminal and will also be stored in generated_problem.txt.
