# n: number of terms
def estimate_PI(n):
    pi = j = 0

    for i in range(1, 2 * n, 2):
        if j % 2 == 0:
            pi += 1 / i
        else:
            pi -= 1 / i
        j += 1

    return pi * 4


def main():

    print ("%.3f" % estimate_PI(6))
    print ("%.3f" % estimate_PI(8))

if __name__ == '__main__':
    main()

