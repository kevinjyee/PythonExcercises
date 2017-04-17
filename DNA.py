# File: DNA.py

# Description: Longest Common Subsequences

# Student Name: Kevin Yee

# Student UT EID: kjy252

# Course Name: CS 303E

# Unique Number: 51580

# Date Created: 032817

# Date Last Modified:
#AT
#CG


resultslist = [];

def print_list(pairnum):
    if len(resultslist) ==0:
        print("Pair",pairnum+1,": No Common Sequence Found");

    maxlength =0;
    currentmaxstring = "";
    #find the number of subsequences that are in the list
    finallist = [];
    for element in resultslist:
        if(len(element)>=maxlength):
            maxlength = len(element)
    for element in resultslist:
        if(len(element) == maxlength):
            finallist.append(element);

    finallist = list(set(finallist))
    if(maxlength==1):
        print("Pair", pairnum + 1, ": No Common Sequence Found");
    else:
        for i in range(len(finallist)):
            if(i==0):
                print("Pair "+str( pairnum + 1)+" :", finallist[i]);
            else:
                print((7 + len(str(i))) * " ", end=" ")
                print(finallist[i]);
        print();
    resultslist.clear();
    finallist.clear();

def find_pair(shorterpair,longerpair):
    searchwindow = len(shorterpair);
    while(searchwindow >0):
        start =0;
        while(start + searchwindow <=len(shorterpair)):
            substrand = shorterpair[start:start + searchwindow];
            if substrand not in longerpair:
                start+=1;
                continue;
            else:
                resultslist.append(substrand);
            start +=1;
        searchwindow -=1;



def find_smaller(pair1,pair2):
    shorter = "";
    longer = "";
    if len(pair1) > len(pair2):
        shorter = pair2;
        longer = pair1;
    else:
        shorter = pair1;
        longer = pair2;
    return shorter,longer;


def main():
    print()
    print("Longest Common Sequences")
    print();
    # read in the text file
    infile = open("dna.txt", "r")
    numpairs = int(infile.readline().strip());
    for i in range(numpairs):
        pair1= infile.readline().strip().upper();
        pair2 = infile.readline().strip().upper();
        shorterpair,longerpair = find_smaller(pair1,pair2)
        find_pair(shorterpair,longerpair);
        print_list(i);
    infile.close;



if __name__ == "__main__":
  main()