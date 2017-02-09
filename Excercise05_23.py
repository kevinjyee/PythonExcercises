'''(Financial application: compare loans with various interest rates) Write a program
that lets the user enter the loan amount and loan period in number of years
and
displays the monthly and total payments for each interest rate starting from
5%
to 8%, with an increment of 1/8. Here is a sample run:'''



def calculate_loans(amount,year):
    monthly =0;

    for i in range(0, 25):
        interest = (5 + i * 0.125) / 100
        monthlyInterestRate = interest / 12
        monthlyPayment = amount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (year * 12))
        totalPayment = monthlyPayment * year * 12
        print(format(interest*100,".3f"));
        print(format(monthlyPayment,".3f"));
        print(format(totalPayment, ".3f"));


def main():
    loanamount = float(input("Enter your loan amount: "))
    loanperiod = int(input("Enter you loan period: "))
    calculate_loans(loanamount,loanperiod);


if __name__ == '__main__':
    main()