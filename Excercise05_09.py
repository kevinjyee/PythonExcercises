'''Excercise 5.9
(Financial application: compute future tuition) Suppose that the tuition for a university
is $10,000 this year and increases 5% every
year.
Write a program that
computes
the tuition in ten years and the total cost of four years’ worth
of tuition
starting
ten years from now.'''



def tuition_in_ten_years(initial,percentincrease):
    for i in range (0,10):
        initial = (initial * percentincrease);
    return initial;

def cost_of_for_years(initial,percentincrease):
    sum =0;
    sum = initial*(1+percentincrease+percentincrease**2+percentincrease**3);
    return sum;

def main():
    initialtuition = 10000;
    percentincrease = 1.05

    costintenyrs = tuition_in_ten_years(initialtuition,percentincrease);
    tuitioninfouryrs = cost_of_for_years(costintenyrs,percentincrease);
    print(costintenyrs);
    print(tuitioninfouryrs);

if __name__ == '__main__':
    main()