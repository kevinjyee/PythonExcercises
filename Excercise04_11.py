'''Find the number of days in a month) Write a program that prompts the user to
enter the month and year and displays the number of days in the month. For example,
if the user entered month
2
and year 2000, the program should display that
February 2000 has 29 days. If the user entered month 3 and year 2005, the program
should display that March 2005 has 31 days.'''

'''
To determine whether a year is a leap year, follow these steps:
If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
The year is a leap year (it has 366 days).
The year is not a leap year (it has 365 days).'''


monthsdict = {1:"January",
              2:"February",
              3:"March",
              4:"April",
              5:"May",
              6:"June",
              7:"July",
              8:"August",
              9:"September",
              10:"October",
              11:"November",
              12:"December"}

daysdict = {1: 31,
              2:28,
              3:31,
              4:30,
              5:31,
              6:30,
              7:31,
              8:31,
              9:30,
              10:31,
              11:30,
              12:31}

def is_leapyear(year):
    if(year % 4 ==0 and year % 100 == 0 and year % 400 ==0):

        return True

    else:
        return False

def main():
    month,year = eval(input("Enter the month and years: "));
    str_month = monthsdict[month];

    isleap = is_leapyear(year);

    if(isleap):
        daysdict[2] = 29;

    num_days = daysdict[month];

    print(str_month,year,"has",num_days, "days")

if __name__ == '__main__':
    main()