# File: Hailstone.py

# Description: Determines the longest cycle length of the hailstone problem

# Student Name: Kevin Yee

# Student UT EID: kjy252

# Course Name: CS 303E

# Unique Number: 51580

# Date Created: 021917

# Date Last Modified:



# simulates hailstone
def find_cycle (start,end):
    maxcycle = 0
    maxpos = 0
    #account for negative numbers
    if(end <= 1):
        return end, 0

    #nested for loop to test cycles
    for i in range(start, end +1):
        currentnum =1
        if(i>0):
            currentnum = i;
        currentnumcycle = 0
        while(currentnum != 1):
            #if Even
            if(currentnum % 2 ==0):
                currentnum = currentnum//2
            else:
                #If odd
                currentnum = currentnum*3+1
            currentnumcycle += 1;
            if(currentnumcycle >= maxcycle):
                maxcycle = currentnumcycle
                maxpos = i

    return maxpos,maxcycle

def main():
    # prompt the user to enter the number of rounds
    start = int (input ("Enter starting number of the range: "))
    while(start < 0):
        start = int (input ("Enter starting number of the range: "))

    end = int(input("Enter ending number of the range: "))
    while(end < 0):
        end = int (input ("Enter ending number of the range: "))

    number,longestcycle = find_cycle(start,end)

    print("The number",number,"has the longest cycle length of",str(longestcycle)+".")

if __name__ == "__main__":
  main()