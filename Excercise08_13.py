'''(Longest common prefix) Write a method that returns the longest common prefix
of two strings. For example, the longest common prefix of distance and
disinfection is dis. The header of the method is:
def prefix(s1, s2)
If the two strings have no common prefix, the method returns an empty string.
Write a main method that prompts the user to enter two strings and displays their
common prefix.'''



def longest_common_prefix(str1, str2):
    i =0;
    prefix = ""
    while str1[i] == str2[i]:
        prefix += str1[i];
        i+=1;
    if(prefix != ""):
        return prefix;
    else:
        return "No common prefix"
def main():
    string1 = str(input("Enter String 1: "))
    string2 = str(input("Enter String 2: "))
    print(longest_common_prefix(string1, string2))
if __name__ == "__main__":
        main()