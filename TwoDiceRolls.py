#  File: Craps.py

#  Description: Simulates sum of two dice rolls. Roll first dice. Then sum second dice based on first dices roll.

#  Student Name: Kevin Yee

#  Date Created: 02/17/2016

#  Date Last Modified:

import random
import statistics


simulatedlist =[];
def diceroll ():
    #
    firstroll = random.randint(1,6)
    secondroll = 0
    for i in range(firstroll):
        secondroll += random.randint(1,6)
    total = firstroll + secondroll
    simulatedlist.append(total);


def main():
    # prompt the user to enter the number of rounds
    num_rounds = int (input ("Enter number of rounds: "))

    # compute the number of times he wins
    num_wins = 0
    for n in range (num_rounds):
        diceroll()

    mean = statistics.mean(simulatedlist);
    stddev = statistics.stdev(simulatedlist);

    print("The mean is", mean, "and the standdeviation is ", stddev)

main()