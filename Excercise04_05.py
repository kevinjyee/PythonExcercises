'''(Find future dates) Write a program that prompts the user to enter an integer for
today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
prompt the user to enter the number of days after today for a future day and display
the future day of the week. Here is a sample ru'''

daysinweek = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

def main():
    dayindex = int(eval(input("Enter today's day: ")));
    elapsed = int(eval(input("Enter the number of days elapsed since today: ")))
    day = daysinweek[dayindex%7]
    futureday = daysinweek[(dayindex + elapsed)%7];

    print("Today is",day,"and the future day is",futureday);



if __name__ == '__main__':
    main()