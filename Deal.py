# File: Deal.py

# Description: Solves Monty Hall Problems

# Student Name: Kevin Yee

# Student UT EID: kjy252

# Course Name: CS 303E

# Unique Number: 51580

# Date Created: 021917

# Date Last Modified:

import random


def print_header():
    print ("%7s%11s%11s%13s" % ("Prize","Guess","View","New Guess"))


#finds other door
def find_door(a,b):
    # find nonchosen door
    c =0
    if ((a == 2 or b == 2 ) and (a == 3or b == 3)): c = 1
    if ((a == 1 or b == 1) and (a ==3 or b == 3)): c = 2
    if ((a == 1or b == 1)and (a == 2 or b == 2)): c = 3
    return c


# simulate the monty hall problem
def deal ():
    #randomize simulation of door
    prizedoor = random.randint(1,3)
    guess = random.randint(1,3)
    view = 0
    newguess = 0

    view = find_door(prizedoor,guess)
    newguess = find_door(guess,view)

    print ("%5d%11d%11d%11d" % (prizedoor,guess,view,newguess))
    if(newguess == prizedoor):
        return 1
    else:
        return 0

    return 0





def main():
    # prompt the user to enter the number of rounds
    num_rounds = int (input ("Enter number of rounds: "))

    # compute the number of times he wins
    num_wins = 0

    print_header()
    for n in range (num_rounds):
        num_wins += deal()

    # print the result
    winpercentage = num_wins/num_rounds
    losepercentage = 1-winpercentage

    print("Probability of winning if you switch = ",end= " ")
    print("%.2f"%winpercentage)
    print("Probability of winning if you do not switch = ",end = " ")
    print("%.2f"%losepercentage)

if __name__ == "__main__":
  main()