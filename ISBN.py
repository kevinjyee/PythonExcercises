#  File: ISBN.py

#  Description: Verifies Correctness of ISBN

#  Student Name: Kevin

#  Student UT EID: kjy252

#  Course Name: CS 303E

#  Unique Number:

#  Date Created: 041517

#  Date Last Modified:

def partialSum(arr):
  arr= list(arr);
  for i in range(1, len(arr)):
    arr[i] = arr[i - 1] + arr[i]
  return arr

def is_ISBNAlgo(arr):
    s1 = partialSum(arr)
    s2 = partialSum(s1)
    return (s2[-1] % 11 == 0)

def is_correctValues(arr):
    for i in range(len(arr)-1):
        if(not arr[i].isdigit()):
            return False;
    return True;

def converStringtoList(arr):
    newlist = [];
    for i in range(len(arr)-1):
        newlist.append(int(arr[i]));
    if(arr[-1].upper() == 'X'):
        newlist.append(10);
    else:
        newlist.append(int(arr[-1]));
    return newlist;

def main():

    infile = open("isbn.txt", "r")
    outfile = open("isbnOut.txt","w");


    for line in infile:
        current_ISBN = line.strip();
        current_ISBN = current_ISBN.replace("-","");

        is_ISBN = (len(current_ISBN) == 10);
        if(is_ISBN):
            is_ISBN =( current_ISBN[-1].isdigit() or current_ISBN[-1] == 'x' or current_ISBN[-1] == 'X')
        if(is_ISBN):
            is_ISBN = is_correctValues(current_ISBN);

        if(is_ISBN):
            listISBN = converStringtoList(current_ISBN);
            is_ISBN = is_ISBNAlgo(listISBN);



        if (is_ISBN):
            outfile.write(line.strip() + "  valid\n")
        else:
            outfile.write(line.strip() + "  invalid\n")

    infile.close();
    outfile.close();
if __name__ == "__main__":
  main()