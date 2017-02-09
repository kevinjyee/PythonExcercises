import math
def main():
    sum =0;
    for i in range(1,625):
        sum += 1/(math.sqrt(i)+math.sqrt(i+1))
    print(sum)

if __name__ == '__main__':
    main()