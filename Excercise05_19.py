'''(Display  a pyramid) Write a program that prompts the user to enter an integer
from 1 to 15 and displays a pyramid, as shown in the following sample run:'''


def drawTriangle(height):
    for i in range(1,height+1):
        for j in range(i,1,-1):
            print(j,end =' ');
        for k in range(1,i+1,1):
            print(k,end =' ');
        print();
    print();




def main():
    height = int(input("Enter a number 1 through 15: "));
    drawTriangle(height);
if __name__ == '__main__':
    main()