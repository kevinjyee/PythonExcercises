'''(Count single digits) Write a program that generates 1,000 random integers
between 0 and 9 and displays the count for each number. (Hint: Use a list of ten
integers, say counts, to store the counts for the number of 0s, 1s, ..., 9s.)'''

import random
def count_nums(randlist):
    count_list = [0]*10;
    for i in range(len(count_list)):
        count_list[i] = randlist.count(i)
    print (count_list);
def main():
    randomlist = [0]*1001;
    for i in range(1000):
        randomlist[i] = random.randint(0,9);
    count_nums(randomlist);
if __name__ == "__main__":
        main()