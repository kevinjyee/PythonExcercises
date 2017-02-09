'''(Geometry: points in triangle?) Suppose a right triangle is placed in a plane as
shown below. The right-angle point is at (0, 0), and the other two points are at
(200, 0), and (0, 100). Write a program that prompts the user to enter a point with
x- and y-coordinates and determines whether the point is inside the triangle. Here
are some sample runs:'''


def main():
  a,b,c = eval(input("Enter three edges: "));
  if(a+b < c or b+c < a or a+c < b):
      print("The input is invalid");
  else:
      print(a+b+c);



if __name__ == '__main__':
    main()