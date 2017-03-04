#  File: Craps.py

#  Description: Simulates a single round of craps

#  Student Name: Kevin Yee

#  Student UT EID: kjy252

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 02/17/2016

#  Date Last Modified:

import random

# simulate a single round of craps and
# return 1 if player wins and 0 if he loses
def craps ():
    #
    firstroll = random.randint(1,6)
    secondroll = random.randint(1,6)
    total = firstroll + secondroll
    pointphase = False


    #if value is 7 or 11, you win
    if(total == 7 or total == 11):
        return 1
    #if value is 2, 3, or 12 you lose
    elif(total == 2 or total == 3 or total == 12):
        return 0
    #if valuse is 4,5,6 or 8,9,10 you enter pointphase
    elif((total >= 4 and total <=6) or (total >= 8 and total <= 10)):
        pointphase = True

    while(pointphase):
        #roll your "point" before you roll 7
        pointroll = random.randint(1,6) + random.randint(1,6)
        if(pointroll == 7):
            pointphase = False
            return 0;
        if(pointroll == total):
            pointphase = False
            return 1
    return 0;

def main():
    # prompt the user to enter the number of rounds
    num_rounds = int (input ("Enter number of rounds: "))

    # compute the number of times he wins
    num_wins = 0
    for n in range (num_rounds):
        num_wins += craps()

    # print the result
    print ("Player wins", num_wins, "out of", num_rounds, "rounds.")

main()