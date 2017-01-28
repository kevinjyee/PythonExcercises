


def main():
    finalAccountValue = eval(input("Enter final account value: " ));
    annualInterestRate = eval(input("Enter annual interest rate in percent: "));
    numYears = eval(input("Enter number of years: "));

    initi = finalAccountValue/((1+annualInterestRate/12/100)**(numYears*12));

    print("Initial deposit value is",initi);
if __name__ == '__main__':
    main()

