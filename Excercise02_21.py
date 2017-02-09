'''Write a program that prompts the user to enter a monthly saving amount and
displays the account value after the sixth month. Here is a sample run of the
program:
'''





def main():
    interest = .05;
    total = 0;
    savings = int(input("Enter the monthly saving amount: "));
    for i in range(0,6):
       savings = savings*(1+interest/12);
       total += savings;
    print("After the sixth month, the account value is ",total);

if __name__ == '__main__':
    main()
