'''10.3(Count occurrence of numbers) Write a program that reads some integers
between 1 and 100 and counts the occurrences of each. Here is a sample run of
the program:'''


def count_numbers(numbers):
    listnums = 101 * [0]
    for i in range(1,100+1):
        listnums[i] = numbers.count(i);
        if(listnums[i] ==1):
            print(i,"occurs 1 time");
        if(listnums[i] > 1):
            print(i, "occurs", listnums[i], "times")

def main():
    # Read numbers as a string from the console
    s = input("Enter a list of numbers between 1 and 100: ")
    items = s.split()  # Extract items from the string
    lst = [eval(x) for x in items]  # Convert items to numbers
    count_numbers(lst)

if __name__ == "__main__":
        main()