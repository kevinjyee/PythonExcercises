'''Compute pi'''


import math


def main():
    for i in range(10000,100000+1,10000):
        summation = 0;
        for j in range(1,i+1,1):
            summation += (math.pow(-1,(j+1)))/(2*j-1)
        print(4.0*summation);

if __name__ == '__main__':
    main()