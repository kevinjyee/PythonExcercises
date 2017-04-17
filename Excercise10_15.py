'''(Sorted?) Write the following function that returns true if the list is already
sorted in increasing order:
def isSorted(lst):
Write a test program that prompts the user to enter a list and displays whether the
list is sorted or not. Here is a sample run:'''

def is_sorted(lst):
    for i in range(1,len(lst)):
        if(lst[i-1] > lst[i]):
            return False;
    return True;


def main():
    s = input("Enter ten numbers: ");
    items = s.split()  # Extract items from the string
    lst = [eval(x) for x in items]  # Convert items to numbers
    TF = is_sorted(lst);
    if(TF):
        print ("The list is already sorted");
    else:
        print ("The list is not sorted")
if __name__ == "__main__":
        main()