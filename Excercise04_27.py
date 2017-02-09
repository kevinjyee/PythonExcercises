'''(Geometry: points in triangle?) Suppose a right triangle is placed in a plane as
shown below. The right-angle point is at (0, 0), and the other two points are at
(200, 0), and (0, 100). Write a program that prompts the user to enter a point with
x- and y-coordinates and determines whether the point is inside the triangle. Here
are some sample runs:'''


def main():
    a,b = eval(input("Enter a point's x- and y-coordinates: "));
    # y = mx + b
    # m = -.5
    # b = 100

    if(a > 200 or b > 100):
        print("The point is not in the triangle");
        return;
    if(b > -.5*a+100):
        print ("The point is not in the triangle");
    else:
        print("The point is in the triangle");





if __name__ == '__main__':
    main()