'''(Print distinct numbers) Write a program that reads in numbers separated by a
space in one line and displays distinct numbers (i.e., if a number appears multiple
times, it is displayed only once). (Hint: Read all the numbers and store them in list1.
Create a new list list2. Add a number in list1 to list2.
If the number is already in the list, ignore it.) Here is the sample run of the
program:'''

def remove_duplicates(numbers):
    nondup = []
    for i in range(len(numbers)):
        if( not numbers[i] in nondup):
            nondup.append(numbers[i]);
    return nondup
def main():
    # Read numbers as a string from the console
    s = input("Enter ten numbers: ");
    items = s.split()  # Extract items from the string
    lst = [eval(x) for x in items]  # Convert items to numbers
    nonduplst = remove_duplicates(lst);
    for i in nonduplst:
        print (i, end=' ');
if __name__ == "__main__":
        main()