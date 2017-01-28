'''(Financial: compare costs) Suppose you shop for rice and find it in two differentsized
packages. You
would
like
to write a program to compare the costs of the
packages.
The program prompts the user to enter the weight and price of each
package
and then displays the one with the better price. Here is a sample run:'''

def main():
    weight1, price1 = eval(input("Enter weight and price for package 1: "))
    weight2, price2 = eval(input("Enter weight and price for package 2: "))
    package1 = price1 / weight1
    package2 = price2 / weight2
    if package1 > package2:
        print("Package 2 has the better price")
    else:
        print("Package 1 has the better price")



if __name__ == '__main__':
    main()