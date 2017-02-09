'''Excercise 01.11

Chapter 1 Exercise 11:
 *      (Population projection) The U.S. Census Bureau projects population based on the following assumptions:
 *          - One birth every 7 seconds
 *          - One death every 13 seconds
 *          - One new immigrant every 45 seconds
 *      Write a program to display the population for each of the next five years.
 *      Assume the current population is 312,032,486 and one year has 365 days.

'''




import math

def calculate_population(POP,YEARS):
    birthRateInSeconds = 7
    deathRateInSeconds = 13
    immigrantsInSeconds = 45
    secondsperYear = 24*60*60*365;

    numBirths = secondsperYear/birthRateInSeconds
    numDeaths = secondsperYear//deathRateInSeconds
    numImmigrants = secondsperYear/immigrantsInSeconds
    for i in range(0,YEARS):
        POP += (numBirths + numImmigrants - numDeaths);
        print(((int(POP))));



def main():
    CURRENT_POPULATION = 312032486;
    YEARS_TO_PROJECT = 5;
    calculate_population(CURRENT_POPULATION,YEARS_TO_PROJECT);

if __name__ == '__main__':
    main()



#314812582#
# 317592679
# #320372776
# #323152873#
# 325932970

