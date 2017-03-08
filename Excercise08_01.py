'''*8.1 (Check SSN) Write a program that prompts the user to enter a Social Security
number in the format ddd-dd-dddd, where d is a digit. The program displays
Valid SSN for a correct Social Security number or Invalid SSN otherwise.'''

def check_valid(num):
    DASH = "-";
    if(str(num[3]) != DASH or str(num[6]) != DASH or len(num) != 11):
        return "Invalid SSN";
    for i in range(len(num)):
        if((not num[i].isdigit() and i!= 3) and (not num[i].isdigit() and i!= 6)):
            return "Invalid SSN";

    return "Valid SSN"
def main():
    number = str(input("Enter a social security number"))
    print (check_valid(number));

if __name__ == "__main__":
        main()