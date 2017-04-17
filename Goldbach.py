'''Every even number greater than or equal to 4 can be expressed as the sum of two prime numbers.
Lower limit is equal to or greater than 4
Both lower limit and upper limit are even
Lower limit is strictly less than upper limit
Enter the lower limit: 4
Enter the upper limit: 100
4 = 2 + 2
6 = 3 + 3
8 = 3 + 5
10 = 3 + 7 = 5 + 5
....
....
100 = ....'''

#  File: Goldbach.py

#  Description: Proves Goldbach's Conjecture

#  Student Name: Kevin Yee

#  Student UT EID: kjy252

#  Course Name: CS 303E

#  Unique Number:

#  Date Created: 03/08/2017

#  Date Last Modified:



#determine is prime
def is_prime(num):
    if(num == 1):
        return False;
    for i in range(2,num//2+1):
        if num % i == 0:
            return False;
    return True;




# find all prime summations in the given range
def find_goldmans(start,end):
    resultslist = [];
    for i in range(start,end+1,2):
        resultslist.append(str(i));
        for j in range(2,i//2+1):
            if(is_prime(j) and is_prime(i-j)):
                resultslist.append("=");
                resultslist.append(str(j));
                resultslist.append("+");
                resultslist.append(str(i-j));
        resultslist = [' {0} '.format(elem) for elem in resultslist];
        print(''.join(resultslist).strip());
        resultslist.clear()


def promptuser():
    start = int(input("Enter the lower limit: "))
    end = int(input("Enter the upper limit: "))
    return start,end


def main():
    # prompt the user to enter the lower limit
    start,end = promptuser();
    while(start < 4 or start %2 != 0 or end%2!=0 or start >= end):
        start,end = promptuser();

    find_goldmans(start,end);

if __name__ == "__main__":
  main()