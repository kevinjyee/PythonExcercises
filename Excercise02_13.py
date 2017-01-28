'''(Split digits) Write a program that prompts the user to enter a four-digit integer
and displays the number in reverse order. Here is a sample run:'''




def main():
    integertoPrint =str(eval(input("Enter an integer: ")));

    integertoPrint[::-1];
    num = int(integertoPrint)
    while(num > 0):
        print(num%10)
        num//=10;


if __name__ == '__main__':
    main()