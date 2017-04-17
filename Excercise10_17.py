'''(Anagrams) Write a function that checks whether two words are anagrams.
Two words are anagrams if they contain the same letters. For example, silent
and listen are anagrams. The header of the function is:
def isAnagram(s1, s2):
(Hint: Obtain two lists for the two strings. Sort the lists and check if two lists
are identical.)
Write a test program that prompts the user to enter two strings and, if they
are anagrams, displays is an anagram; otherwise, it displays is not an
anagram
.'''

def is_anagram(s1,s2):
    if(len(s1) != len(s2)):
        return False;
    return sorted(s1) == sorted(s2);



def main():
    s1 = input("Enter string 1: ");
    s2 = input("Enter string 2: ")
    TF = is_anagram(s1,s2);
    if(TF):
        print ("are anagram");
    else:
        print("is not anagram");
if __name__ == "__main__":
        main()