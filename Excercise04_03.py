'''*4.3 (Algebra: solve linear equations) You can use Cramer’s rule to solve the
following system of linear equation:
2 * 2
2 * 2
ax + by = e
cx + dy = f
  x =
ed - bf
ad - bc
  y =
af - ec
ad - bc
Write a program that prompts the user to enter
a, b, c, d, e, and f and display the
result. If ad – bc is 0, report that The equation has no solution.'''


def main():
    a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

    x = (e*d - b*f)/(a*d - b*c);
    y = (a*f - e*c)/(a*d - b*c);

    if a*d - b*c == 0:
        print("The equation has no solution");
    else:
        print("x is ",x,"and y is",y);


if __name__ == '__main__':
    main()