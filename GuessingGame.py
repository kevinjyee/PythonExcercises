#  File: GuessingGame.py

#  Description: Solves a Guessing Game

#  Student Name: Kevin Yee

#  Student UT EID: kjy252

#  Course Name: CS 303E

#  Unique Number:

#  Date Created: 04/10/17

#  Date Last Modified: 04/10/17



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


def print_header():
    print();
    print("Guessing Game");
    print();
    print("Think of a number between 1 and 100 inclusive.");
    print("And I will think what it is in 7 tries or less");
    print();
    response = "";
    while(response != 'y'):
        response = input("Are you ready? (y/n): ");
        if(response == 'n'):
            break;
    return response;

def main():
    if(print_header() =="n"):
        print("Bye");
        return;
    print();
    low = 0;
    high = 100;
    for numguess in range(1,8):
        mid = (high+low)//2;
        print("Guess ",numguess, ": ","The number you thought was",int(mid));
        print("Enter 1 if my guess was high, -1 if low, and 0 if correct: -1");
        userresponse = int(input());
        while(userresponse > 1 or userresponse <-1):
            print("Guess ", numguess, ": ", "The number you thought was", int(mid));
            print("Enter 1 if my guess was high, -1 if low, and 0 if correct: -1");
            userresponse = int(input());
        if(userresponse==1):
            high = mid;
        elif(userresponse==-1):
            low= mid +1;
        elif(userresponse ==0):
            break;

    print("Thank you for playing the Guessing Game.", end='\n');


if __name__ == "__main__":
  main()