'''(Occurrences of a specified string) Write a function that counts the occurrences of a
specified non-overlapping string
s2 in another string s1 using the following header:
def count(s1, s2):
For example, count("system error, syntax error", "error") returns
2. Write a test program that prompts the user to enter two strings and displays the
number of occurrences of the second string in the first string.'''


def main():
    firststring = str(input("Enter first string"))
    secondstring = str(input("Enter the second string"))

    print(firststring.count(secondstring));
if __name__ == "__main__":
        main()