#  File: Grid.py

#  Description: Find greatest product in a grid.txt

#  Student Name: Kevin Yee

#  Student UT EID: kjy252

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 303E

#  Unique Number:

#  Date Created: 042217

#  Date Last Modified: 042217


#Globals
DIMENSIONS =0
MAXPROD =0

def populate_grid(grid):
    # read in the text file
    infile = open("grid.txt", "r")

    #read the Dimensions of the grid.txt
    global DIMENSIONS;
    DIMENSIONS = infile.readline().strip();
    DIMENSIONS = int(DIMENSIONS);

    #populate the grid.txt
    for i in range(DIMENSIONS):
        line = infile.readline().strip()
        row = line.split();
        for j in range(DIMENSIONS):
            row[j] = int(row[j]);
        grid.append(row);

    return

def greatest_row(grid):
    # read each row in blocks of four
    global MAXPROD
    for row in grid:
        for i in range(DIMENSIONS - 3):
            prod = 1
            for j in range(i, i + 4):
                prod = prod * row[j]
            if(prod >= MAXPROD):
                MAXPROD = prod;

    return


def greatest_column(grid):
    # read each column in blocks of four
    global MAXPROD
    for j in range(DIMENSIONS):
        for i in range(DIMENSIONS - 3):
            prod = 1
            for k in range(i, i + 4):
                prod = prod * grid[k][j]
            if (prod >= MAXPROD):
                MAXPROD = prod;
    return

def greatest_LRdiagonal(grid):
    global MAXPROD
# go along all diagonals L to R in blocks of 4
    for i in range(DIMENSIONS - 3):
        for j in range(DIMENSIONS - 3):
            prod =1
            for k in range(4):
                prod = grid[i + k][j + k]*prod;
            if(prod>=MAXPROD):
                MAXPROD = prod;

def greatest_RLdiagonal(grid):
    global MAXPROD
# go along all diagonals L to R in blocks of 4
    for i in range(DIMENSIONS - 3):
        for j in range(DIMENSIONS - 3):
            prod =1
            for k in range(4):
                prod = grid[i+k][DIMENSIONS-1-j -k]*prod;
            if(prod>=MAXPROD):
                MAXPROD = prod;

def main():
    #create a new empty grid
    grid = [];
    populate_grid(grid);
    greatest_row(grid);
    greatest_column(grid);
    greatest_LRdiagonal(grid);
    greatest_RLdiagonal(grid);
    print();
    print("The greatest product is",MAXPROD);


if __name__ == "__main__":
  main()