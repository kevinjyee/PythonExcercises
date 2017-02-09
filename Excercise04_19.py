'''(Compute the perimeter of a triangle) Write a program that reads three edges for a
triangle and computes the perimeter if the input is valid. Otherwise, display that
the input is invalid. The input is valid if the sum of every pair of two edges is
greater than the remaining edge. Here is a sample run'''


def main():
  a,b,c = eval(input("Enter three edges: "));
  if(a+b < c or b+c < a or a+c < b):
      print("The input is invalid");
  else:
      print(a+b+c);



if __name__ == '__main__':
    main()