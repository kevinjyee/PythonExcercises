'''(Math: combinations) Write a program that displays all possible combinations for
picking two numbers from integers 1 to 7. Also display the total number of combinations.'''

import math

def main():
    count =0;
    for i in range(1,8):
        for j in range(i,8):
            if(j >i):
                print(i," ",j);
                count +=1;

    #count = math.factorial(7)/(math.factorial(2)*math.factorial(7-2))
    print("The total number of all combinations is ",int(count))
if __name__ == '__main__':
    main()